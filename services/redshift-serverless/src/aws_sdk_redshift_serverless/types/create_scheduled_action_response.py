"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateScheduledActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.scheduled_action_response


class CreateScheduledActionResponse(TypedDict, closed=True):
    scheduled_action: NotRequired[
        "aws_sdk_redshift_serverless.types.scheduled_action_response.ScheduledActionResponse"
    ]
    """<p>The returned <code>ScheduledAction</code> object that describes the properties of a scheduled action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action" in value:
        import aws_sdk_redshift_serverless.types.scheduled_action_response

        out["scheduledAction"] = (
            aws_sdk_redshift_serverless.types.scheduled_action_response.serialize_aws_json_1_1(
                value["scheduled_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScheduledActionResponse:
    out: CreateScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAction" in data:
        import aws_sdk_redshift_serverless.types.scheduled_action_response

        out["scheduled_action"] = (
            aws_sdk_redshift_serverless.types.scheduled_action_response.deserialize_aws_json_1_1(
                data["scheduledAction"]
            )
        )
    return out
