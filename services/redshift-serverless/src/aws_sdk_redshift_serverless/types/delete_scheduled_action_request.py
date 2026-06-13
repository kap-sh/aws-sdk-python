"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteScheduledActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.scheduled_action_name


class DeleteScheduledActionRequest(TypedDict):
    scheduled_action_name: (
        "aws_sdk_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    )
    """<p>The name of the scheduled action to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScheduledActionRequest) -> dict:
    out: dict = {}
    out["scheduledActionName"] = value["scheduled_action_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScheduledActionRequest:
    out: DeleteScheduledActionRequest = {}  # type: ignore[typeddict-item]
    if "scheduledActionName" in data:
        out["scheduled_action_name"] = data["scheduledActionName"]
    else:
        raise DeserializationError(
            "DeleteScheduledActionRequest.scheduled_action_name required"
        )
    return out
