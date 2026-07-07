"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_version


class GetAdapterVersionRequest(TypedDict, closed=True):
    adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId"
    """<p>A string specifying a unique ID for the adapter version you want to retrieve information for.</p>"""
    adapter_version: "aws_sdk_textract.types.adapter_version.AdapterVersion"
    """<p>A string specifying the adapter version you want to retrieve information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterVersionRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    out["AdapterVersion"] = value["adapter_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterVersionRequest:
    out: GetAdapterVersionRequest = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    else:
        raise DeserializationError("GetAdapterVersionRequest.adapter_id required")
    if "AdapterVersion" in data:
        out["adapter_version"] = data["AdapterVersion"]
    else:
        raise DeserializationError("GetAdapterVersionRequest.adapter_version required")
    return out
