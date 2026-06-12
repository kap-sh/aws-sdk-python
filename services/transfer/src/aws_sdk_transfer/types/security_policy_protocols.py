"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyProtocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.security_policy_protocol

SecurityPolicyProtocols: TypeAlias = list[
    "aws_sdk_transfer.types.security_policy_protocol.SecurityPolicyProtocol"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityPolicyProtocols) -> list:
    import aws_sdk_transfer.types.security_policy_protocol

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transfer.types.security_policy_protocol.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityPolicyProtocols:
    import aws_sdk_transfer.types.security_policy_protocol

    out: SecurityPolicyProtocols = []
    for item in data:
        out.append(
            aws_sdk_transfer.types.security_policy_protocol.deserialize_aws_json_1_1(
                item
            )
        )
    return out
