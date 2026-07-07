"""Generated from Smithy shape ``com.amazonaws.cloudhsm#AddTagsToResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.string


class AddTagsToResourceResponse(TypedDict, closed=True):
    status: "aws_sdk_cloudhsm.types.string.String"
    """<p>The status of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceResponse) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceResponse:
    out: AddTagsToResourceResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("AddTagsToResourceResponse.status required")
    return out
