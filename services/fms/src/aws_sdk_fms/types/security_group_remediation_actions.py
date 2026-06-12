"""Generated from Smithy shape ``com.amazonaws.fms#SecurityGroupRemediationActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.security_group_remediation_action

SecurityGroupRemediationActions: TypeAlias = list[
    "aws_sdk_fms.types.security_group_remediation_action.SecurityGroupRemediationAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupRemediationActions) -> list:
    import aws_sdk_fms.types.security_group_remediation_action

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.security_group_remediation_action.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityGroupRemediationActions:
    import aws_sdk_fms.types.security_group_remediation_action

    out: SecurityGroupRemediationActions = []
    for item in data:
        out.append(
            aws_sdk_fms.types.security_group_remediation_action.deserialize_aws_json_1_1(
                item
            )
        )
    return out
