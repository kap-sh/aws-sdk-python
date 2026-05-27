"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFlowLogsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item_set


class DeleteFlowLogsResult(TypedDict):
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the flow logs that could not be deleted successfully.</p>"""
