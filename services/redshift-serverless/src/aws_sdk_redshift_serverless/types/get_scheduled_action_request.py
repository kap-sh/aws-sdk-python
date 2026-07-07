"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetScheduledActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.scheduled_action_name


class GetScheduledActionRequest(TypedDict, closed=True):
    scheduled_action_name: (
        "aws_sdk_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    )
    """<p>The name of the scheduled action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledActionRequest) -> dict:
    out: dict = {}
    out["scheduledActionName"] = value["scheduled_action_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledActionRequest:
    out: GetScheduledActionRequest = {}  # type: ignore[typeddict-item]
    if "scheduledActionName" in data:
        out["scheduled_action_name"] = data["scheduledActionName"]
    else:
        raise DeserializationError(
            "GetScheduledActionRequest.scheduled_action_name required"
        )
    return out
