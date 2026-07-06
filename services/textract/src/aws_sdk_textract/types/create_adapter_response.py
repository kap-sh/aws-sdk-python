"""Generated from Smithy shape ``com.amazonaws.textract#CreateAdapterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id


class CreateAdapterResponse(TypedDict, closed=True):
    adapter_id: NotRequired["aws_sdk_textract.types.adapter_id.AdapterId"]
    """<p>A string containing the unique ID for the adapter that has been created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdapterResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdapterResponse:
    out: CreateAdapterResponse = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    return out
