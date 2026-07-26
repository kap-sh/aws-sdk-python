"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailInsightsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.email_insights

EmailInsightsList: TypeAlias = list["capo_sesv2.types.email_insights.EmailInsights"]


# --- restJson1 ser/de ---
def serialize_json(value: EmailInsightsList) -> list:
    import capo_sesv2.types.email_insights

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.email_insights.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailInsightsList:
    import capo_sesv2.types.email_insights

    out: EmailInsightsList = []
    for item in data:
        out.append(capo_sesv2.types.email_insights.deserialize_json(item))
    return out
