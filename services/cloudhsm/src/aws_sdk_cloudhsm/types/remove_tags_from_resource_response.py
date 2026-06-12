"""Generated from Smithy shape ``com.amazonaws.cloudhsm#RemoveTagsFromResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.string


class RemoveTagsFromResourceResponse(TypedDict):
    status: "aws_sdk_cloudhsm.types.string.String"
    """<p>The status of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceResponse) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceResponse:
    out: RemoveTagsFromResourceResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("RemoveTagsFromResourceResponse.status required")
    return out
