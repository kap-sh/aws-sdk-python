"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.match_item

MatchesList: TypeAlias = list["capo_customer_profiles.types.match_item.MatchItem"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchesList) -> list:
    import capo_customer_profiles.types.match_item

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.match_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchesList:
    import capo_customer_profiles.types.match_item

    out: MatchesList = []
    for item in data:
        out.append(capo_customer_profiles.types.match_item.deserialize_json(item))
    return out
