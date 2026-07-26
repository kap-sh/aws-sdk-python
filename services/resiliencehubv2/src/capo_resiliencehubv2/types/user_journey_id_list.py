"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourneyIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.user_journey_id

UserJourneyIdList: TypeAlias = list[
    "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserJourneyIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserJourneyIdList:
    return list(data)
