"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteAgentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.batch_delete_agent_errors


class BatchDeleteAgentsResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_application_discovery_service.types.batch_delete_agent_errors.BatchDeleteAgentErrors"
    ]
    """<p> A list of agent IDs that failed to delete during the deletion task, each paired with an error message. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteAgentsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_application_discovery_service.types.batch_delete_agent_errors

        out["errors"] = (
            aws_sdk_application_discovery_service.types.batch_delete_agent_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteAgentsResponse:
    out: BatchDeleteAgentsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_application_discovery_service.types.batch_delete_agent_errors

        out["errors"] = (
            aws_sdk_application_discovery_service.types.batch_delete_agent_errors.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
