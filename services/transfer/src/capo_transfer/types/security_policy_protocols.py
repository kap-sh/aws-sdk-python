"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyProtocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.security_policy_protocol

SecurityPolicyProtocols: TypeAlias = list[
    "capo_transfer.types.security_policy_protocol.SecurityPolicyProtocol"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityPolicyProtocols) -> list:
    import capo_transfer.types.security_policy_protocol

    out: list = []
    for item in value:
        out.append(
            capo_transfer.types.security_policy_protocol.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityPolicyProtocols:
    import capo_transfer.types.security_policy_protocol

    out: SecurityPolicyProtocols = []
    for item in data:
        out.append(
            capo_transfer.types.security_policy_protocol.deserialize_aws_json_1_1(item)
        )
    return out
