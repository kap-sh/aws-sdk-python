"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetScheduledActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.scheduled_action_response


class GetScheduledActionResponse(TypedDict, closed=True):
    scheduled_action: NotRequired[
        "capo_redshift_serverless.types.scheduled_action_response.ScheduledActionResponse"
    ]
    """<p>The returned scheduled action object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledActionResponse) -> dict:
    out: dict = {}
    if "scheduled_action" in value:
        import capo_redshift_serverless.types.scheduled_action_response

        out["scheduledAction"] = (
            capo_redshift_serverless.types.scheduled_action_response.serialize_aws_json_1_1(
                value["scheduled_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledActionResponse:
    out: GetScheduledActionResponse = {}  # type: ignore[typeddict-item]
    if "scheduledAction" in data:
        import capo_redshift_serverless.types.scheduled_action_response

        out["scheduled_action"] = (
            capo_redshift_serverless.types.scheduled_action_response.deserialize_aws_json_1_1(
                data["scheduledAction"]
            )
        )
    return out
