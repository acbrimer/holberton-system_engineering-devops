# Puppet setup file for key only ssh

file {'/etc/ssh/ssh_config':
    content => '    PasswordAuthentication no
    IdentityFile ~/.ssh/holberton
'
}
