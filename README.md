# ansible-role-packer-incus

This is an ansible role. this role will build alma8, alma9, opensuse tumbleweed, ubuntu 20, ubuntu 22, ubuntu 24 incus images by packer.

## usages:
add this role with your image builde server.

```
cat incus-image.yml
---
- hosts: images
  become: yes
  gather_facts: true

  roles:
    - ansible-role-packer-incus
```


## License
BSD

## Author Information
khabir uddin
masumndc1@gmail.com
