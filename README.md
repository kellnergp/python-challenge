# python-challenge

## PyBank
As a preliminary step, I imported os and csv as dependencies, set the paths for input and output, and read in the .csv file from resources.

First, I generated lists for months and profits for each month then used a for loop to populate them from the csv file.

Next, the number of months and total profit were determined with the len() and sum() functions respectively.

To find change in profits from month to month I generated an index ranging from 1 to len(months)  and used that in a loop to subtract previous month profits from current month profits.

The average change in profits was the sum of the change list divided by the length of the change list.

Max and min change were found using the native functions and checked in a loop against the change list to find the proper months, adjusting for alignment with the original months list by adding 1.

Analysis was handled with a succession of strings printed to terminal and written to a text file.

## PyPoll
After importing dependencies and reading in the .csv, the first step was to create a list for vote values and populate it by appending values from the csv.

Next, I stored the length of the votes list as total_votes and generated an empty list for candidates.

The candidate list was populated with a for loop looking for values not in the candidate list, thus selecting out all unique values.

I then generated a list of the index values for the candidates and created a list for vote_counts starting with a 0-value for each candidate.

The vote_counts list was populated by looping through the votes, checking each entry against the candidate list and adding 1 to vote_counts in the appropriate entryfor each candidate.

Vote percentages were calculated by dividing final vote_counts by total_votes and winning count was determined with the max() function.

Winner was pulled by comparing winning value to the vote count list in a for loop and using its index value to pull the winning candidate name.

Analysis strings were created based on the template in the assignment, using variables to pull required values and names, using a loop to create a list of strings with the detailed results for each candidate.

The strings were printed to terminal and written to a text file in the order required to fit the template.
