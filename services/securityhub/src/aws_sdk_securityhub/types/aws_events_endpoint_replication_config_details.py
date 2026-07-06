"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointReplicationConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEventsEndpointReplicationConfigDetails(TypedDict, closed=True):
    state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The state of event replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventsEndpointReplicationConfigDetails) -> dict:
    out: dict = {}
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_json(data: dict) -> AwsEventsEndpointReplicationConfigDetails:
    out: AwsEventsEndpointReplicationConfigDetails = {}  # type: ignore[typeddict-item]
    if "State" in data:
        out["state"] = data["State"]
    return out
