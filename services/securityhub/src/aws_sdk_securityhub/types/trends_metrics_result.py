"""Generated from Smithy shape ``com.amazonaws.securityhub#TrendsMetricsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.timestamp
    import aws_sdk_securityhub.types.trends_values


class TrendsMetricsResult(TypedDict):
    timestamp: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for this data point in the findings trend metrics.</p>"""
    trends_values: NotRequired["aws_sdk_securityhub.types.trends_values.TrendsValues"]
    """<p>The finding trend metric values associated with this timestamp, including severity counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrendsMetricsResult) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_securityhub.types.timestamp

        out["Timestamp"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "trends_values" in value:
        import aws_sdk_securityhub.types.trends_values

        out["TrendsValues"] = aws_sdk_securityhub.types.trends_values.serialize_json(
            value["trends_values"]
        )
    return out


def deserialize_json(data: dict) -> TrendsMetricsResult:
    out: TrendsMetricsResult = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_securityhub.types.timestamp

        out["timestamp"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "TrendsValues" in data:
        import aws_sdk_securityhub.types.trends_values

        out["trends_values"] = aws_sdk_securityhub.types.trends_values.deserialize_json(
            data["TrendsValues"]
        )
    return out
