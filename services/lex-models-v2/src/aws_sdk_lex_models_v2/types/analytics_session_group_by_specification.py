"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionGroupBySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_field


class AnalyticsSessionGroupBySpecification(TypedDict, closed=True):
    name: "aws_sdk_lex_models_v2.types.analytics_session_field.AnalyticsSessionField"
    """<p>Specifies whether to group the session by their end state or their locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionGroupBySpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_session_field

    out["name"] = aws_sdk_lex_models_v2.types.analytics_session_field.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsSessionGroupBySpecification:
    out: AnalyticsSessionGroupBySpecification = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_session_field

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_session_field.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsSessionGroupBySpecification.name required")
    return out
