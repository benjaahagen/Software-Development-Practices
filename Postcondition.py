import random

class Class:
    
    #Generate a given amount of random numbers between a range of numbers.
    def random_number_generator(amount, minRange, maxRange):

        assert isinstance(amount, int) #Precondition 1 - amount shold be an integer.
        assert minRange >= 0 #Precondition 2 - consider only positive numbers.
        assert minRange < maxRange #Precondition 3 - minRange should be less than maxRange.

        random_numbers = []
        for i in range(amount):
            random_numbers.append(random.randint(minRange, maxRange))

        assert len(random_numbers) == amount #Postcondition 1 - there should only be an expected amount of random numbers.
        assert min(random_numbers) >= minRange #Postcondition 2 - all the random numbers should be greater than or equal to minRange.
        assert max(random_numbers) <= maxRange #Postcondition 3 - all the random numbers should be less than or equal to maxRange.

        return random_numbers

x = Class.random_number_generator(10, 1, 100)
print (x)