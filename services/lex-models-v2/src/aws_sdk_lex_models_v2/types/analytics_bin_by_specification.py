"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinBySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_bin_by_name
    import aws_sdk_lex_models_v2.types.analytics_interval
    import aws_sdk_lex_models_v2.types.analytics_sort_order


class AnalyticsBinBySpecification(TypedDict, closed=True):
    name: "aws_sdk_lex_models_v2.types.analytics_bin_by_name.AnalyticsBinByName"
    """<p>Specifies the time metric by which to bin the analytics data.</p>"""
    interval: "aws_sdk_lex_models_v2.types.analytics_interval.AnalyticsInterval"
    """<p>Specifies the interval of time by which to bin the analytics data.</p>"""
    order: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    ]
    """<p>Specifies whether to bin the analytics data in ascending or descending order. If this field is left blank, the default order is by the key of the bin in descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsBinBySpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_bin_by_name

    out["name"] = aws_sdk_lex_models_v2.types.analytics_bin_by_name.serialize_json(
        value["name"]
    )
    import aws_sdk_lex_models_v2.types.analytics_interval

    out["interval"] = aws_sdk_lex_models_v2.types.analytics_interval.serialize_json(
        value["interval"]
    )
    if "order" in value:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = aws_sdk_lex_models_v2.types.analytics_sort_order.serialize_json(
            value["order"]
        )
    return out


def deserialize_json(data: dict) -> AnalyticsBinBySpecification:
    out: AnalyticsBinBySpecification = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_bin_by_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_bin_by_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsBinBySpecification.name required")
    if "interval" in data:
        import aws_sdk_lex_models_v2.types.analytics_interval

        out["interval"] = (
            aws_sdk_lex_models_v2.types.analytics_interval.deserialize_json(
                data["interval"]
            )
        )
    else:
        raise DeserializationError("AnalyticsBinBySpecification.interval required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = (
            aws_sdk_lex_models_v2.types.analytics_sort_order.deserialize_json(
                data["order"]
            )
        )
    return out
