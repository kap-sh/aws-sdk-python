"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipPoolResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_pool


class CreateCoipPoolResult(TypedDict):
    coip_pool: NotRequired["aws_sdk_ec2.types.coip_pool.CoipPool"]
    """<p>Information about the CoIP address pool.</p>"""
