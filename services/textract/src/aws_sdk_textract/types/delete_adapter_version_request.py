"""Generated from Smithy shape ``com.amazonaws.textract#DeleteAdapterVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_version


class DeleteAdapterVersionRequest(TypedDict):
    adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId"
    """<p>A string containing a unique ID for the adapter version that will be deleted.</p>"""
    adapter_version: "aws_sdk_textract.types.adapter_version.AdapterVersion"
    """<p>Specifies the adapter version to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAdapterVersionRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    out["AdapterVersion"] = value["adapter_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAdapterVersionRequest:
    out: DeleteAdapterVersionRequest = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    else:
        raise DeserializationError("DeleteAdapterVersionRequest.adapter_id required")
    if "AdapterVersion" in data:
        out["adapter_version"] = data["AdapterVersion"]
    else:
        raise DeserializationError(
            "DeleteAdapterVersionRequest.adapter_version required"
        )
    return out
