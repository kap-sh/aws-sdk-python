"""Generated from Smithy shape ``com.amazonaws.textract#UpdateAdapterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_description
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_name
    import aws_sdk_textract.types.auto_update
    import aws_sdk_textract.types.date_time
    import aws_sdk_textract.types.feature_types


class UpdateAdapterResponse(TypedDict):
    adapter_id: NotRequired["aws_sdk_textract.types.adapter_id.AdapterId"]
    """<p>A string containing a unique ID for the adapter that has been updated.</p>"""
    adapter_name: NotRequired["aws_sdk_textract.types.adapter_name.AdapterName"]
    """<p>A string containing the name of the adapter that has been updated.</p>"""
    creation_time: NotRequired["aws_sdk_textract.types.date_time.DateTime"]
    """<p>An object specifying the creation time of the the adapter that has been updated.</p>"""
    description: NotRequired[
        "aws_sdk_textract.types.adapter_description.AdapterDescription"
    ]
    """<p>A string containing the description of the adapter that has been updated.</p>"""
    feature_types: NotRequired["aws_sdk_textract.types.feature_types.FeatureTypes"]
    """<p>List of the targeted feature types for the updated adapter.</p>"""
    auto_update: NotRequired["aws_sdk_textract.types.auto_update.AutoUpdate"]
    """<p>The auto-update status of the adapter that has been updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAdapterResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_name" in value:
        out["AdapterName"] = value["adapter_name"]
    if "creation_time" in value:
        import aws_sdk_textract.types.date_time

        out["CreationTime"] = aws_sdk_textract.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "feature_types" in value:
        import aws_sdk_textract.types.feature_types

        out["FeatureTypes"] = (
            aws_sdk_textract.types.feature_types.serialize_aws_json_1_1(
                value["feature_types"]
            )
        )
    if "auto_update" in value:
        import aws_sdk_textract.types.auto_update

        out["AutoUpdate"] = aws_sdk_textract.types.auto_update.serialize_aws_json_1_1(
            value["auto_update"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAdapterResponse:
    out: UpdateAdapterResponse = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    if "AdapterName" in data:
        out["adapter_name"] = data["AdapterName"]
    if "CreationTime" in data:
        import aws_sdk_textract.types.date_time

        out["creation_time"] = (
            aws_sdk_textract.types.date_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "FeatureTypes" in data:
        import aws_sdk_textract.types.feature_types

        out["feature_types"] = (
            aws_sdk_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    if "AutoUpdate" in data:
        import aws_sdk_textract.types.auto_update

        out["auto_update"] = (
            aws_sdk_textract.types.auto_update.deserialize_aws_json_1_1(
                data["AutoUpdate"]
            )
        )
    return out
