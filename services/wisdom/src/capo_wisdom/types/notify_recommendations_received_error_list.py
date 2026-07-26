"""Generated from Smithy shape ``com.amazonaws.wisdom#NotifyRecommendationsReceivedErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.notify_recommendations_received_error

NotifyRecommendationsReceivedErrorList: TypeAlias = list[
    "capo_wisdom.types.notify_recommendations_received_error.NotifyRecommendationsReceivedError"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedErrorList) -> list:
    import capo_wisdom.types.notify_recommendations_received_error

    out: list = []
    for item in value:
        out.append(
            capo_wisdom.types.notify_recommendations_received_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotifyRecommendationsReceivedErrorList:
    import capo_wisdom.types.notify_recommendations_received_error

    out: NotifyRecommendationsReceivedErrorList = []
    for item in data:
        out.append(
            capo_wisdom.types.notify_recommendations_received_error.deserialize_json(
                item
            )
        )
    return out
