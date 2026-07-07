"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnStackDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_stack_id
    import aws_sdk_sagemaker.types.cfn_stack_name
    import aws_sdk_sagemaker.types.cfn_stack_status_message


class CfnStackDetail(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.cfn_stack_name.CfnStackName"]
    """<p> The name of the CloudFormation stack. </p>"""
    id: NotRequired["aws_sdk_sagemaker.types.cfn_stack_id.CfnStackId"]
    """<p> The unique identifier of the CloudFormation stack. </p>"""
    status_message: NotRequired[
        "aws_sdk_sagemaker.types.cfn_stack_status_message.CfnStackStatusMessage"
    ]
    """<p> A human-readable message about the stack's current status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnStackDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CfnStackDetail:
    out: CfnStackDetail = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
