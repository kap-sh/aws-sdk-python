"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentGroupBySpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_field


class AnalyticsIntentGroupBySpecification(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_intent_field.AnalyticsIntentField"
    """<p>Specifies whether to group the intent stages by their name or their end state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentGroupBySpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_intent_field

    out["name"] = aws_sdk_lex_models_v2.types.analytics_intent_field.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentGroupBySpecification:
    out: AnalyticsIntentGroupBySpecification = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_field

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_field.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsIntentGroupBySpecification.name required")
    return out
