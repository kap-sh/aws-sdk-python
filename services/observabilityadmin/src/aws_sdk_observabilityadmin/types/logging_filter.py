"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LoggingFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.filter_behavior
    import aws_sdk_observabilityadmin.types.filters


class LoggingFilter(TypedDict, closed=True):
    filters: NotRequired["aws_sdk_observabilityadmin.types.filters.Filters"]
    """<p> A list of filter conditions that determine log record handling behavior. </p>"""
    default_behavior: NotRequired[
        "aws_sdk_observabilityadmin.types.filter_behavior.FilterBehavior"
    ]
    """<p> The default action (KEEP or DROP) for log records that don't match any filter conditions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingFilter) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_observabilityadmin.types.filters

        out["Filters"] = aws_sdk_observabilityadmin.types.filters.serialize_json(
            value["filters"]
        )
    if "default_behavior" in value:
        import aws_sdk_observabilityadmin.types.filter_behavior

        out["DefaultBehavior"] = (
            aws_sdk_observabilityadmin.types.filter_behavior.serialize_json(
                value["default_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingFilter:
    out: LoggingFilter = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_observabilityadmin.types.filters

        out["filters"] = aws_sdk_observabilityadmin.types.filters.deserialize_json(
            data["Filters"]
        )
    if "DefaultBehavior" in data:
        import aws_sdk_observabilityadmin.types.filter_behavior

        out["default_behavior"] = (
            aws_sdk_observabilityadmin.types.filter_behavior.deserialize_json(
                data["DefaultBehavior"]
            )
        )
    return out
