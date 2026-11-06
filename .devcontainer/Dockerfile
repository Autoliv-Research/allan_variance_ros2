FROM ros:kilted-ros-core

ARG USERNAME=username
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Update Ubuntu user to use the username in args
RUN if [ "$USERNAME" != "root" ]; then \
  usermod -l $USERNAME -d /home/$USERNAME -m ubuntu \
  && groupmod -n $USERNAME ubuntu; \
  fi

RUN apt-get update && apt-get install -y git python3-colcon-common-extensions python3-pip python3-rosdep libeigen3-dev ros-kilted-rosbag2 && rm -rf /var/lib/apt/lists/*

# Remove need of password for sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN curl -L https://github.com/foxglove/mcap/releases/download/releases%2Fmcap-cli%2Fv0.0.40/mcap-linux-amd64 --output /usr/bin/mcap
RUN chmod +x /usr/bin/mcap

USER $USERNAME