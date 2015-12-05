%{
Written by: Sreyas Misra November 23, 2015 

Tested using Matlab R2014a

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

This script analyzes GFP changes in time-lapse microscope videos.
%}

v = VideoReader('1mT_IscA1_Timelapse.avi');
% Reads in 1MT video timelapse by creating VR object 

frames = read(v,[1,Inf]);
% Reads all the frames in the video

[row,col,color,num] = size(frames);
% Get dimensions

images = [];
normFluo = [];
singCell = [];

radius = 40;
% Cell radius %

interval = 10;
% length of time interval between frames %

for i = 1:num
    
    I = frames(:,:,:,i);
    I = rgb2gray(I);
    
    % Make Gaussian filter (width = 3*sigma to remove discontinuities). %

    G = fspecial('gaussian',[15 15],5);
    I = imfilter(I,G,'same');
    
    % Use Otsu's Method to Find Threshold %
    
    level = graythresh(I);
    threshold =  double(((max(max(I)) - min(min(I))))*level + min(min(I)));
    BW1 = roicolor(I,threshold,max(max(I)));
    BW2 = roicolor(I,min(min(I)),threshold);
    Area1 = sum(I(BW1))/sum(sum(BW1));
    Area2 = sum(I(BW2))/sum(sum(BW2));
    threshold = (Area1 - Area2)/2 + Area2;
    
    % Apply Threshold to Image to floor sub-threshold pixels %
    
    for rw = 1:1:row
        for cl = 1:1:col
            if I(rw,cl) <= threshold
                I(rw,cl) = 0;
            end
        end
    end
    % total normalized fluorescence %%%%%%%%%%%%
    [r,c] = find(I > 0);
    
    normFluo = [normFluo, sum(sum(I))/length(r)];
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    % 1-cell fluorescence - pick hotspot cell %%
    
    
    
    % Find hotspot cell range %
    
    [x, y] = find(I == max(max(I)));
    
    sumFluo = 0;
    
    % +/- cells radius at x and y centers %
    for j = (round(mean(x))-radius):(round(mean(x))+radius)
        for k = (round(mean(y))-radius):(round(mean(y))+radius)
            
            sumFluo = I(j,k) + sumFluo;
        end
    end
    
    singCell = [singCell, sum(sum(I((round(mean(x))-radius): ...
    (round(mean(x))+radius),(round(mean(y))-radius): ...
    (round(mean(y))+radius))))/(radius^2)];

     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
end

t = 1:interval:num*interval;

plot(t,normFluo)
title('1MT - Normalized Fluorescence for Time-Lapse Microscope FOV')
xlabel('Time (seconds)')
ylabel('Grayscale Fluorescence Intensity')
figure(2)
plot(t,singCell)
title('1MT - Fluorescence of a single cell')
xlabel('Time (seconds)')
ylabel('Grayscale Fluorescence Intensity')


    
