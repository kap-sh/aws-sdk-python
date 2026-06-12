"""Generated from Smithy shape ``com.amazonaws.textract#DeleteAdapterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id


class DeleteAdapterRequest(TypedDict):
    adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId"
    """<p>A string containing a unique ID for the adapter to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAdapterRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAdapterRequest:
    out: DeleteAdapterRequest = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    else:
        raise DeserializationError("DeleteAdapterRequest.adapter_id required")
    return out
