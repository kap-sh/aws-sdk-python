"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeKeyPairsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.key_pair_list


class DescribeKeyPairsResult(TypedDict):
    key_pairs: NotRequired["aws_sdk_ec2.types.key_pair_list.KeyPairList"]
    """<p>Information about the key pairs.</p>"""
