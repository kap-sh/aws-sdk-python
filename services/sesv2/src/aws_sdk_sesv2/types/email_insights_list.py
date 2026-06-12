"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailInsightsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_insights

EmailInsightsList: TypeAlias = list["aws_sdk_sesv2.types.email_insights.EmailInsights"]


# --- restJson1 ser/de ---
def serialize_json(value: EmailInsightsList) -> list:
    import aws_sdk_sesv2.types.email_insights

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.email_insights.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailInsightsList:
    import aws_sdk_sesv2.types.email_insights

    out: EmailInsightsList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.email_insights.deserialize_json(item))
    return out
