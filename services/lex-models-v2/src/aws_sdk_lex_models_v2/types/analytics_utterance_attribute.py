"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_attribute_name


class AnalyticsUtteranceAttribute(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_utterance_attribute_name.AnalyticsUtteranceAttributeName"
    """<p>An attribute to return. The only available attribute is the intent that the bot mapped the utterance to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceAttribute) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_utterance_attribute_name

    out["name"] = (
        aws_sdk_lex_models_v2.types.analytics_utterance_attribute_name.serialize_json(
            value["name"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceAttribute:
    out: AnalyticsUtteranceAttribute = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_attribute_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_attribute_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsUtteranceAttribute.name required")
    return out
