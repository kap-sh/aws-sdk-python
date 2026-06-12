"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceGroupBySpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_utterance_field


class AnalyticsUtteranceGroupBySpecification(TypedDict):
    name: (
        "aws_sdk_lex_models_v2.types.analytics_utterance_field.AnalyticsUtteranceField"
    )
    """<p>Specifies whether to group the utterances by their text or their state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsUtteranceGroupBySpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_utterance_field

    out["name"] = aws_sdk_lex_models_v2.types.analytics_utterance_field.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsUtteranceGroupBySpecification:
    out: AnalyticsUtteranceGroupBySpecification = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_utterance_field

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_utterance_field.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsUtteranceGroupBySpecification.name required"
        )
    return out
