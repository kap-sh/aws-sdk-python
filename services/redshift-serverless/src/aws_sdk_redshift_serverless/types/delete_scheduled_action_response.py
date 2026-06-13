"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteScheduledActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.scheduled_action_response


class DeleteScheduledActionResponse(TypedDict):
    scheduled_action: NotRequired[
        "aws_sdk_redshift_serverless.types.scheduled_action_response.ScheduledActionResponse"
    ]
    """<p>The deleted scheduled action object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action" in value:
        import aws_sdk_redshift_serverless.types.scheduled_action_response

        out["scheduledAction"] = (
            aws_sdk_redshift_serverless.types.scheduled_action_response.serialize_aws_json_1_1(
                value["scheduled_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScheduledActionResponse:
    out: DeleteScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAction" in data:
        import aws_sdk_redshift_serverless.types.scheduled_action_response

        out["scheduled_action"] = (
            aws_sdk_redshift_serverless.types.scheduled_action_response.deserialize_aws_json_1_1(
                data["scheduledAction"]
            )
        )
    return out
