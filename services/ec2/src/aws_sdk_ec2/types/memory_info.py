"""Generated from Smithy shape ``com.amazonaws.ec2#MemoryInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.memory_size


class MemoryInfo(TypedDict):
    size_in_mi_b: NotRequired["aws_sdk_ec2.types.memory_size.MemorySize"]
    """<p>The size of the memory, in MiB.</p>"""
