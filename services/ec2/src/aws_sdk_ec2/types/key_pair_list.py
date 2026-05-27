"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.key_pair_info

KeyPairList: TypeAlias = list["aws_sdk_ec2.types.key_pair_info.KeyPairInfo"]
