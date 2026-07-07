"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_version
    import aws_sdk_textract.types.adapter_version_status
    import aws_sdk_textract.types.adapter_version_status_message
    import aws_sdk_textract.types.date_time
    import aws_sdk_textract.types.feature_types


class AdapterVersionOverview(TypedDict, closed=True):
    adapter_id: NotRequired["aws_sdk_textract.types.adapter_id.AdapterId"]
    """<p>A unique identifier for the adapter associated with a given adapter version.</p>"""
    adapter_version: NotRequired[
        "aws_sdk_textract.types.adapter_version.AdapterVersion"
    ]
    """<p>An identified for a given adapter version.</p>"""
    creation_time: NotRequired["aws_sdk_textract.types.date_time.DateTime"]
    """<p>The date and time that a given adapter version was created.</p>"""
    feature_types: NotRequired["aws_sdk_textract.types.feature_types.FeatureTypes"]
    """<p>The feature types that the adapter version is operating on.</p>"""
    status: NotRequired[
        "aws_sdk_textract.types.adapter_version_status.AdapterVersionStatus"
    ]
    """<p>Contains information on the status of a given adapter version.</p>"""
    status_message: NotRequired[
        "aws_sdk_textract.types.adapter_version_status_message.AdapterVersionStatusMessage"
    ]
    """<p>A message explaining the status of a given adapter vesion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionOverview) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    if "creation_time" in value:
        import aws_sdk_textract.types.date_time

        out["CreationTime"] = aws_sdk_textract.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "feature_types" in value:
        import aws_sdk_textract.types.feature_types

        out["FeatureTypes"] = (
            aws_sdk_textract.types.feature_types.serialize_aws_json_1_1(
                value["feature_types"]
            )
        )
    if "status" in value:
        import aws_sdk_textract.types.adapter_version_status

        out["Status"] = (
            aws_sdk_textract.types.adapter_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdapterVersionOverview:
    out: AdapterVersionOverview = {}  # type: ignore[typeddict-item]
    if "AdapterId" in data:
        out["adapter_id"] = data["AdapterId"]
    if "AdapterVersion" in data:
        out["adapter_version"] = data["AdapterVersion"]
    if "CreationTime" in data:
        import aws_sdk_textract.types.date_time

        out["creation_time"] = (
            aws_sdk_textract.types.date_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FeatureTypes" in data:
        import aws_sdk_textract.types.feature_types

        out["feature_types"] = (
            aws_sdk_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    if "Status" in data:
        import aws_sdk_textract.types.adapter_version_status

        out["status"] = (
            aws_sdk_textract.types.adapter_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
