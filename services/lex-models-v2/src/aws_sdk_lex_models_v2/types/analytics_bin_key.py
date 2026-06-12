"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_bin_by_name
    import aws_sdk_lex_models_v2.types.analytics_bin_value


class AnalyticsBinKey(TypedDict):
    name: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_bin_by_name.AnalyticsBinByName"
    ]
    """<p>The criterion by which to bin the results.</p>"""
    value: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_bin_value.AnalyticsBinValue"
    ]
    """<p>The value of the criterion that defines the bin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsBinKey) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_lex_models_v2.types.analytics_bin_by_name

        out["name"] = aws_sdk_lex_models_v2.types.analytics_bin_by_name.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AnalyticsBinKey:
    out: AnalyticsBinKey = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_bin_by_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_bin_by_name.deserialize_json(
                data["name"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
