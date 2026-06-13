"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRetryPolicyEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.grpc_retry_policy_event

GrpcRetryPolicyEvents: TypeAlias = list[
    "aws_sdk_app_mesh.types.grpc_retry_policy_event.GrpcRetryPolicyEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRetryPolicyEvents) -> list:
    return list(value)


def deserialize_json(data: list) -> GrpcRetryPolicyEvents:
    return list(data)
