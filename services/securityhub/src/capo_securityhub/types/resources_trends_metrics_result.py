"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsMetricsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resources_trends_values
    import capo_securityhub.types.timestamp


class ResourcesTrendsMetricsResult(TypedDict, closed=True):
    timestamp: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for this data point in the resources trend metrics.</p>"""
    trends_values: NotRequired[
        "capo_securityhub.types.resources_trends_values.ResourcesTrendsValues"
    ]
    """<p>The resource trend metric values associated with this timestamp, including resource counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsMetricsResult) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_securityhub.types.timestamp

        out["Timestamp"] = capo_securityhub.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "trends_values" in value:
        import capo_securityhub.types.resources_trends_values

        out["TrendsValues"] = (
            capo_securityhub.types.resources_trends_values.serialize_json(
                value["trends_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcesTrendsMetricsResult:
    out: ResourcesTrendsMetricsResult = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import capo_securityhub.types.timestamp

        out["timestamp"] = capo_securityhub.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if "TrendsValues" in data:
        import capo_securityhub.types.resources_trends_values

        out["trends_values"] = (
            capo_securityhub.types.resources_trends_values.deserialize_json(
                data["TrendsValues"]
            )
        )
    return out
