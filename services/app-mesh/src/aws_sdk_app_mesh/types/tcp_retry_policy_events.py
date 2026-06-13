"""Generated from Smithy shape ``com.amazonaws.appmesh#TcpRetryPolicyEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.tcp_retry_policy_event

TcpRetryPolicyEvents: TypeAlias = list[
    "aws_sdk_app_mesh.types.tcp_retry_policy_event.TcpRetryPolicyEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TcpRetryPolicyEvents) -> list:
    return list(value)


def deserialize_json(data: list) -> TcpRetryPolicyEvents:
    return list(data)
