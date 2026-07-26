"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.partner_app_arn
    import capo_sagemaker.types.partner_app_name
    import capo_sagemaker.types.partner_app_status
    import capo_sagemaker.types.partner_app_type
    import capo_sagemaker.types.timestamp


class PartnerAppSummary(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App.</p>"""
    name: NotRequired["capo_sagemaker.types.partner_app_name.PartnerAppName"]
    """<p>The name of the SageMaker Partner AI App.</p>"""
    type: NotRequired["capo_sagemaker.types.partner_app_type.PartnerAppType"]
    """<p>The type of SageMaker Partner AI App to create. Must be one of the following: <code>lakera-guard</code>, <code>comet</code>, <code>deepchecks-llm-evaluation</code>, or <code>fiddler</code>.</p>"""
    status: NotRequired["capo_sagemaker.types.partner_app_status.PartnerAppStatus"]
    """<p>The status of the SageMaker Partner AI App.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the SageMaker Partner AI App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_sagemaker.types.partner_app_type

        out["Type"] = capo_sagemaker.types.partner_app_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_sagemaker.types.partner_app_status

        out["Status"] = capo_sagemaker.types.partner_app_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.partner_app_type

        out["type"] = capo_sagemaker.types.partner_app_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Status" in data:
        import capo_sagemaker.types.partner_app_status

        out["status"] = (
            capo_sagemaker.types.partner_app_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
