"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id


class GetAdapterRequest(TypedDict):
    adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId"
    """<p>A string containing a unique ID for the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterRequest:
    out: GetAdapterRequest = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    else:
        raise DeserializationError("GetAdapterRequest.adapter_id required")
    return out
