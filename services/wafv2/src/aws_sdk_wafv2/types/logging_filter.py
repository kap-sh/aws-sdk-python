"""Generated from Smithy shape ``com.amazonaws.wafv2#LoggingFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.filter_behavior
    import aws_sdk_wafv2.types.filters


class LoggingFilter(TypedDict, closed=True):
    filters: "aws_sdk_wafv2.types.filters.Filters"
    """<p>The filters that you want to apply to the logs. </p>"""
    default_behavior: "aws_sdk_wafv2.types.filter_behavior.FilterBehavior"
    """<p>Default handling for logs that don't match any of the specified filtering conditions. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingFilter) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.filters

    out["Filters"] = aws_sdk_wafv2.types.filters.serialize_aws_json_1_1(
        value["filters"]
    )
    import aws_sdk_wafv2.types.filter_behavior

    out["DefaultBehavior"] = aws_sdk_wafv2.types.filter_behavior.serialize_aws_json_1_1(
        value["default_behavior"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingFilter:
    out: LoggingFilter = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_wafv2.types.filters

        out["filters"] = aws_sdk_wafv2.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        raise DeserializationError("LoggingFilter.filters required")
    if "DefaultBehavior" in data:
        import aws_sdk_wafv2.types.filter_behavior

        out["default_behavior"] = (
            aws_sdk_wafv2.types.filter_behavior.deserialize_aws_json_1_1(
                data["DefaultBehavior"]
            )
        )
    else:
        raise DeserializationError("LoggingFilter.default_behavior required")
    return out
