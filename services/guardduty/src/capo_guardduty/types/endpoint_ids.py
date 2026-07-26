"""Generated from Smithy shape ``com.amazonaws.guardduty#EndpointIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

EndpointIds: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointIds) -> list:
    return list(value)


def deserialize_json(data: list) -> EndpointIds:
    return list(data)
