"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionApprovalConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.role_arn


class ExecutionApprovalConfiguration(TypedDict):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    approval_role: "aws_sdk_arc_region_switch.types.role_arn.RoleArn"
    """<p>The IAM approval role for the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionApprovalConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    out["approvalRole"] = value["approval_role"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionApprovalConfiguration:
    out: ExecutionApprovalConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "approvalRole" in data:
        out["approval_role"] = data["approvalRole"]
    else:
        raise DeserializationError(
            "ExecutionApprovalConfiguration.approval_role required"
        )
    return out
