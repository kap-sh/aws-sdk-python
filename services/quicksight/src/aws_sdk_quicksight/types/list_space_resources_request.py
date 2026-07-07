"""Generated from Smithy shape ``com.amazonaws.quicksight#ListSpaceResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.public_space_id


class ListSpaceResourcesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to list resources for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpaceResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSpaceResourcesRequest:
    out: ListSpaceResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
