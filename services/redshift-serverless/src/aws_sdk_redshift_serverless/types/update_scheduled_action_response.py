"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateScheduledActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.scheduled_action_response


class UpdateScheduledActionResponse(TypedDict, closed=True):
    scheduled_action: NotRequired[
        "aws_sdk_redshift_serverless.types.scheduled_action_response.ScheduledActionResponse"
    ]
    """<p>The ScheduledAction object that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action" in value:
        import aws_sdk_redshift_serverless.types.scheduled_action_response

        out["scheduledAction"] = (
            aws_sdk_redshift_serverless.types.scheduled_action_response.serialize_aws_json_1_1(
                value["scheduled_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScheduledActionResponse:
    out: UpdateScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAction" in data:
        import aws_sdk_redshift_serverless.types.scheduled_action_response

        out["scheduled_action"] = (
            aws_sdk_redshift_serverless.types.scheduled_action_response.deserialize_aws_json_1_1(
                data["scheduledAction"]
            )
        )
    return out
