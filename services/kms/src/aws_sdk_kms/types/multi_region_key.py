"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKey``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.arn_type
    import aws_sdk_kms.types.region_type


class MultiRegionKey(TypedDict):
    arn: NotRequired["aws_sdk_kms.types.arn_type.ArnType"]
    """<p>Displays the key ARN of a primary or replica key of a multi-Region key.</p>"""
    region: NotRequired["aws_sdk_kms.types.region_type.RegionType"]
    """<p>Displays the Amazon Web Services Region of a primary or replica key in a multi-Region key.</p>"""
