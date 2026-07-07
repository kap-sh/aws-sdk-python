"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.nullable_boolean


class TopicConfigOptions(TypedDict, closed=True):
    q_business_insights_enabled: NotRequired[
        "aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables Amazon Q Business Insights for a <code>Topic</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicConfigOptions) -> dict:
    out: dict = {}
    if "q_business_insights_enabled" in value:
        out["QBusinessInsightsEnabled"] = value["q_business_insights_enabled"]
    return out


def deserialize_json(data: dict) -> TopicConfigOptions:
    out: TopicConfigOptions = {}  # type: ignore[typeddict-item]
    if "QBusinessInsightsEnabled" in data:
        out["q_business_insights_enabled"] = data["QBusinessInsightsEnabled"]
    return out
