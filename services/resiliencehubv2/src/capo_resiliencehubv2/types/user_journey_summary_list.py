"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourneySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.user_journey_summary

UserJourneySummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.user_journey_summary.UserJourneySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserJourneySummaryList) -> list:
    import capo_resiliencehubv2.types.user_journey_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.user_journey_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserJourneySummaryList:
    import capo_resiliencehubv2.types.user_journey_summary

    out: UserJourneySummaryList = []
    for item in data:
        out.append(
            capo_resiliencehubv2.types.user_journey_summary.deserialize_json(item)
        )
    return out
