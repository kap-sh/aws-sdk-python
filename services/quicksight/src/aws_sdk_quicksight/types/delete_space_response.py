"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteSpaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.public_space_arn
    import aws_sdk_quicksight.types.public_space_id


class DeleteSpaceResponse(TypedDict):
    space_id: "aws_sdk_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["aws_sdk_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSpaceResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteSpaceResponse:
    out: DeleteSpaceResponse = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("DeleteSpaceResponse.space_id required")
    if "spaceArn" in data:
        out["space_arn"] = data["spaceArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
