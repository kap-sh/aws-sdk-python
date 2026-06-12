"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteAgentErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.batch_delete_agent_error

BatchDeleteAgentErrors: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.batch_delete_agent_error.BatchDeleteAgentError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteAgentErrors) -> list:
    import aws_sdk_application_discovery_service.types.batch_delete_agent_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.batch_delete_agent_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteAgentErrors:
    import aws_sdk_application_discovery_service.types.batch_delete_agent_error

    out: BatchDeleteAgentErrors = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.batch_delete_agent_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
