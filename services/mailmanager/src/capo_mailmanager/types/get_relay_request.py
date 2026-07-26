"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetRelayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.relay_id


class GetRelayRequest(TypedDict, closed=True):
    relay_id: "capo_mailmanager.types.relay_id.RelayId"
    """<p>A unique relay identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRelayRequest) -> dict:
    out: dict = {}
    out["RelayId"] = value["relay_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRelayRequest:
    out: GetRelayRequest = {}  # type: ignore[typeddict-item]
    if "RelayId" in data:
        out["relay_id"] = data["RelayId"]
    else:
        raise DeserializationError("GetRelayRequest.relay_id required")
    return out
