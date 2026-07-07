"""Generated from Smithy shape ``com.amazonaws.ssmincidents#SsmAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.dynamic_ssm_parameters
    import aws_sdk_ssm_incidents.types.role_arn
    import aws_sdk_ssm_incidents.types.ssm_parameters
    import aws_sdk_ssm_incidents.types.ssm_target_account


class SsmAutomation(TypedDict, closed=True):
    role_arn: "aws_sdk_ssm_incidents.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.</p>"""
    document_name: "str"
    """<p>The automation document's name.</p>"""
    document_version: NotRequired["str"]
    """<p>The automation document's version to use when running.</p>"""
    target_account: NotRequired[
        "aws_sdk_ssm_incidents.types.ssm_target_account.SsmTargetAccount"
    ]
    """<p>The account that the automation document will be run in. This can be in either the management account or an application account.</p>"""
    parameters: NotRequired["aws_sdk_ssm_incidents.types.ssm_parameters.SsmParameters"]
    """<p>The key-value pair parameters to use when running the automation document.</p>"""
    dynamic_parameters: NotRequired[
        "aws_sdk_ssm_incidents.types.dynamic_ssm_parameters.DynamicSsmParameters"
    ]
    """<p>The key-value pair to resolve dynamic parameter values when processing a Systems Manager Automation runbook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmAutomation) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["documentName"] = value["document_name"]
    if "document_version" in value:
        out["documentVersion"] = value["document_version"]
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "parameters" in value:
        import aws_sdk_ssm_incidents.types.ssm_parameters

        out["parameters"] = aws_sdk_ssm_incidents.types.ssm_parameters.serialize_json(
            value["parameters"]
        )
    if "dynamic_parameters" in value:
        import aws_sdk_ssm_incidents.types.dynamic_ssm_parameters

        out["dynamicParameters"] = (
            aws_sdk_ssm_incidents.types.dynamic_ssm_parameters.serialize_json(
                value["dynamic_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SsmAutomation:
    out: SsmAutomation = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("SsmAutomation.role_arn required")
    if "documentName" in data:
        out["document_name"] = data["documentName"]
    else:
        raise DeserializationError("SsmAutomation.document_name required")
    if "documentVersion" in data:
        out["document_version"] = data["documentVersion"]
    if "targetAccount" in data:
        out["target_account"] = data["targetAccount"]
    if "parameters" in data:
        import aws_sdk_ssm_incidents.types.ssm_parameters

        out["parameters"] = aws_sdk_ssm_incidents.types.ssm_parameters.deserialize_json(
            data["parameters"]
        )
    if "dynamicParameters" in data:
        import aws_sdk_ssm_incidents.types.dynamic_ssm_parameters

        out["dynamic_parameters"] = (
            aws_sdk_ssm_incidents.types.dynamic_ssm_parameters.deserialize_json(
                data["dynamicParameters"]
            )
        )
    return out
