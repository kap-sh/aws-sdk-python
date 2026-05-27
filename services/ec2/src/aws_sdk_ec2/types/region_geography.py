"""Generated from Smithy shape ``com.amazonaws.ec2#RegionGeography``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class RegionGeography(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the geography, for example, <code>United States of America</code>.</p>"""
