# ansible-role-packer-incus

This is an ansible role. This role will build alma8, alma9,
ubuntu 20, ubuntu 22, ubuntu 24, opensuse tumbleweed incus images by packer.

This images will have:
  - an pre-defined user installed,
  - sudo right to that user,
  - add public key of that user in ssh folder,
  - and ssh service running.

## usages:
Add this role with your image builde server.

```
cat incus-image.yml
---
- hosts: images
  become: yes
  gather_facts: true

  roles:
    - ansible-role-packer-incus
```

For example:

```
root@image-server # incus image list
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
|      ALIAS      | FINGERPRINT  | PUBLIC |               DESCRIPTION                | ARCHITECTURE |   TYPE    |   SIZE    |     UPLOAD DATE      |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
| alma8-packer    | cc974abbfc9c | no     | incus alma8 repackage with Packer        | aarch64      | CONTAINER | 222.55MiB | 2024/06/06 14:17 UTC |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
| alma9-packer    | 5e369db8c197 | no     | incus alma9 repackage with Packer        | aarch64      | CONTAINER | 169.00MiB | 2024/06/06 14:19 UTC |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
| opensuse-packer | 20a055080f6d | no     | incus opensuse repackage with Packer     | aarch64      | CONTAINER | 104.58MiB | 2024/06/06 14:27 UTC |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
| ubu20-packer    | 9f2cfcb2231a | no     | incus ubuntu 20 repackage with Packer    | aarch64      | CONTAINER | 178.59MiB | 2024/06/06 14:32 UTC |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
| ubu22-packer    | 790c1eeeb704 | no     | incus ubuntu 22 repackage with Packer    | aarch64      | CONTAINER | 190.84MiB | 2024/06/06 15:03 UTC |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
| ubu24-packer    | 270d829dccdb | no     | incus ubuntu 24 repackage with Packer    | aarch64      | CONTAINER | 194.81MiB | 2024/06/06 16:47 UTC |
+-----------------+--------------+--------+------------------------------------------+--------------+-----------+-----------+----------------------+
```

## License
BSD

## Author Information
khabir uddin
masumndc1@gmail.com
