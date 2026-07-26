"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateScheduledActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.scheduled_action_response


class UpdateScheduledActionResponse(TypedDict, closed=True):
    scheduled_action: NotRequired[
        "capo_redshift_serverless.types.scheduled_action_response.ScheduledActionResponse"
    ]
    """<p>The ScheduledAction object that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action" in value:
        import capo_redshift_serverless.types.scheduled_action_response

        out["scheduledAction"] = (
            capo_redshift_serverless.types.scheduled_action_response.serialize_aws_json_1_1(
                value["scheduled_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScheduledActionResponse:
    out: UpdateScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAction" in data:
        import capo_redshift_serverless.types.scheduled_action_response

        out["scheduled_action"] = (
            capo_redshift_serverless.types.scheduled_action_response.deserialize_aws_json_1_1(
                data["scheduledAction"]
            )
        )
    return out
