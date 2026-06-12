"""Generated from Smithy shape ``com.amazonaws.textract#CreateAdapterVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_version


class CreateAdapterVersionResponse(TypedDict):
    adapter_id: NotRequired["aws_sdk_textract.types.adapter_id.AdapterId"]
    """<p>A string containing the unique ID for the adapter that has received a new version.</p>"""
    adapter_version: NotRequired[
        "aws_sdk_textract.types.adapter_version.AdapterVersion"
    ]
    """<p>A string describing the new version of the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdapterVersionResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdapterVersionResponse:
    out: CreateAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    if "AdapterVersion" in data:
        out["adapter_version"] = data["AdapterVersion"]
    return out
