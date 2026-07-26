"""Generated from Smithy shape ``com.amazonaws.novaact#S3KeyPrefix``."""

from typing import TypeAlias

"""A prefix for S3 object keys that will be prepended to 'step_{N}.json'. Must follow S3 object key naming guidelines and cannot end with a forward slash as it will be directly concatenated with the filename."""
S3KeyPrefix: TypeAlias = str
