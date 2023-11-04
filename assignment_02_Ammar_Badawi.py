def count_digits_recursive(num):
  if num < 10:
    return 1
  return 1 + count_digits_recursive(num // 10)


def find_max_recursive(numbers):
  if len(numbers) == 0:
    return 0
  if len(numbers) == 1:
    return numbers[0]
  else:
    sub_max = find_max_recursive(numbers[1:])
    return numbers[0] if numbers[0] > sub_max else sub_max


def count_tags_recursive(html, tag):
  start_tag = f"<{tag}>"
  end_tag = f"</{tag}>"
  count = 0
  start_index = 0
  while start_index < len(html):
    start_index = html.find(start_tag, start_index)
    if start_index == -1:
      break
    end_index = html.find(end_tag, start_index)
    if end_index == -1:
      break
    count += 1
    start_index = end_index + len(end_tag)
  return count


while True:
  print("1. Count Digits")
  print("2. Find Max")
  print("3. Count Tags")
  print("4. Exit")
  choice = input("Enter a choice: ")

  if choice == '1':
    num = int(input("Enter an integer: "))
    digit_count = count_digits_recursive(abs(num))
    print(f"Number of digits: {digit_count}")
  elif choice == '2':
    numbers = [
        int(x) for x in input(
            "Enter a list of integers (comma-separated): ").split(',')
    ]
    max_value = find_max_recursive(numbers)
    print(f"Maximum value: {max_value}")
  elif choice == '3':
    html = '''<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>'''
    tag = input("Enter HTML tag: ")
    tag_count = count_tags_recursive(html, tag)
    print(f"Occurrences of '{tag}' tag: {tag_count}")
  elif choice == '4':
    break
  else:
    print("Invalid choice. Please enter a valid option.")
