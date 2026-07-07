"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.communication_limit_time_unit


class CommunicationLimit(TypedDict, closed=True):
    max_count_per_recipient: "int"
    """Maximum number of contacts allowed for a given target within the given frequency."""
    frequency: "int"
    """The number of days to consider with regards to this limit."""
    unit: "aws_sdk_connectcampaignsv2.types.communication_limit_time_unit.CommunicationLimitTimeUnit"


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationLimit) -> dict:
    out: dict = {}
    out["maxCountPerRecipient"] = value["max_count_per_recipient"]
    out["frequency"] = value["frequency"]
    out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> CommunicationLimit:
    out: CommunicationLimit = {}  # type: ignore[typeddict-item]
    if "maxCountPerRecipient" in data:
        out["max_count_per_recipient"] = data["maxCountPerRecipient"]
    else:
        raise DeserializationError(
            "CommunicationLimit.max_count_per_recipient required"
        )
    if "frequency" in data:
        out["frequency"] = data["frequency"]
    else:
        raise DeserializationError("CommunicationLimit.frequency required")
    if "unit" in data:
        out["unit"] = data["unit"]
    else:
        raise DeserializationError("CommunicationLimit.unit required")
    return out
