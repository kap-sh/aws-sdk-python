"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.partner_app_arn
    import aws_sdk_sagemaker.types.partner_app_name
    import aws_sdk_sagemaker.types.partner_app_status
    import aws_sdk_sagemaker.types.partner_app_type
    import aws_sdk_sagemaker.types.timestamp


class PartnerAppSummary(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App.</p>"""
    name: NotRequired["aws_sdk_sagemaker.types.partner_app_name.PartnerAppName"]
    """<p>The name of the SageMaker Partner AI App.</p>"""
    type: NotRequired["aws_sdk_sagemaker.types.partner_app_type.PartnerAppType"]
    """<p>The type of SageMaker Partner AI App to create. Must be one of the following: <code>lakera-guard</code>, <code>comet</code>, <code>deepchecks-llm-evaluation</code>, or <code>fiddler</code>.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.partner_app_status.PartnerAppStatus"]
    """<p>The status of the SageMaker Partner AI App.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the SageMaker Partner AI App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_sagemaker.types.partner_app_type

        out["Type"] = aws_sdk_sagemaker.types.partner_app_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_sagemaker.types.partner_app_status

        out["Status"] = (
            aws_sdk_sagemaker.types.partner_app_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerAppSummary:
    out: PartnerAppSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.partner_app_type

        out["type"] = aws_sdk_sagemaker.types.partner_app_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.partner_app_status

        out["status"] = (
            aws_sdk_sagemaker.types.partner_app_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
