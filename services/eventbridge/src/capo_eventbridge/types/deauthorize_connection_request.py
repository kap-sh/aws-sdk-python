"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeauthorizeConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_name


class DeauthorizeConnectionRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.connection_name.ConnectionName"
    """<p>The name of the connection to remove authorization from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeauthorizeConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeauthorizeConnectionRequest:
    out: DeauthorizeConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeauthorizeConnectionRequest.name required")
    return out
