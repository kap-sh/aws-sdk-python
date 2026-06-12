"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsMetricsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_trends_values
    import aws_sdk_securityhub.types.timestamp


class ResourcesTrendsMetricsResult(TypedDict):
    timestamp: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for this data point in the resources trend metrics.</p>"""
    trends_values: NotRequired[
        "aws_sdk_securityhub.types.resources_trends_values.ResourcesTrendsValues"
    ]
    """<p>The resource trend metric values associated with this timestamp, including resource counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsMetricsResult) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_securityhub.types.timestamp

        out["Timestamp"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "trends_values" in value:
        import aws_sdk_securityhub.types.resources_trends_values

        out["TrendsValues"] = (
            aws_sdk_securityhub.types.resources_trends_values.serialize_json(
                value["trends_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcesTrendsMetricsResult:
    out: ResourcesTrendsMetricsResult = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_securityhub.types.timestamp

        out["timestamp"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "TrendsValues" in data:
        import aws_sdk_securityhub.types.resources_trends_values

        out["trends_values"] = (
            aws_sdk_securityhub.types.resources_trends_values.deserialize_json(
                data["TrendsValues"]
            )
        )
    return out
