"""Generated from Smithy shape ``com.amazonaws.textract#UpdateAdapterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_description
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_name
    import aws_sdk_textract.types.auto_update


class UpdateAdapterRequest(TypedDict):
    adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId"
    """<p>A string containing a unique ID for the adapter that will be updated.</p>"""
    description: NotRequired[
        "aws_sdk_textract.types.adapter_description.AdapterDescription"
    ]
    """<p>The new description to be applied to the adapter.</p>"""
    adapter_name: NotRequired["aws_sdk_textract.types.adapter_name.AdapterName"]
    """<p>The new name to be applied to the adapter.</p>"""
    auto_update: NotRequired["aws_sdk_textract.types.auto_update.AutoUpdate"]
    """<p>The new auto-update status to be applied to the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAdapterRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "adapter_name" in value:
        out["AdapterName"] = value["adapter_name"]
    if "auto_update" in value:
        import aws_sdk_textract.types.auto_update

        out["AutoUpdate"] = aws_sdk_textract.types.auto_update.serialize_aws_json_1_1(
            value["auto_update"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAdapterRequest:
    out: UpdateAdapterRequest = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    else:
        raise DeserializationError("UpdateAdapterRequest.adapter_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "AdapterName" in data:
        out["adapter_name"] = data["AdapterName"]
    if "AutoUpdate" in data:
        import aws_sdk_textract.types.auto_update

        out["auto_update"] = (
            aws_sdk_textract.types.auto_update.deserialize_aws_json_1_1(
                data["AutoUpdate"]
            )
        )
    return out
