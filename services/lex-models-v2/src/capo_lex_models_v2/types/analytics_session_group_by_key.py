"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionGroupByKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_group_by_value
    import capo_lex_models_v2.types.analytics_session_field


class AnalyticsSessionGroupByKey(TypedDict, closed=True):
    name: NotRequired[
        "capo_lex_models_v2.types.analytics_session_field.AnalyticsSessionField"
    ]
    """<p>The category by which the session analytics were grouped.</p>"""
    value: NotRequired[
        "capo_lex_models_v2.types.analytics_group_by_value.AnalyticsGroupByValue"
    ]
    """<p>A member of the category by which the session analytics were grouped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionGroupByKey) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_lex_models_v2.types.analytics_session_field

        out["name"] = capo_lex_models_v2.types.analytics_session_field.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AnalyticsSessionGroupByKey:
    out: AnalyticsSessionGroupByKey = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_lex_models_v2.types.analytics_session_field

        out["name"] = capo_lex_models_v2.types.analytics_session_field.deserialize_json(
            data["name"]
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
