"""Generated from Smithy shape ``com.amazonaws.guardduty#IpSetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

IpSetIds: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: IpSetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> IpSetIds:
    return list(data)
