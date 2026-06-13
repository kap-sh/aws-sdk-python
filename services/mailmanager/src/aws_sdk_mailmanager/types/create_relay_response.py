"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateRelayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.relay_id


class CreateRelayResponse(TypedDict):
    relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId"
    """<p>A unique identifier of the created relay resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelayResponse) -> dict:
    out: dict = {}
    out["RelayId"] = value["relay_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelayResponse:
    out: CreateRelayResponse = {}  # type: ignore[typeddict-item]
    if "RelayId" in data:
        out["relay_id"] = data["RelayId"]
    else:
        raise DeserializationError("CreateRelayResponse.relay_id required")
    return out
