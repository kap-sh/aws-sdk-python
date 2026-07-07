"""Generated from Smithy shape ``com.amazonaws.securityhub#TrendsValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.severity_trends_count


class TrendsValues(TypedDict, closed=True):
    severity_trends: NotRequired[
        "aws_sdk_securityhub.types.severity_trends_count.SeverityTrendsCount"
    ]
    """<p>The count of findings organized by severity level for this data point in the trend timeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrendsValues) -> dict:
    out: dict = {}
    if "severity_trends" in value:
        import aws_sdk_securityhub.types.severity_trends_count

        out["SeverityTrends"] = (
            aws_sdk_securityhub.types.severity_trends_count.serialize_json(
                value["severity_trends"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrendsValues:
    out: TrendsValues = {}  # type: ignore[typeddict-item]
    if "SeverityTrends" in data:
        import aws_sdk_securityhub.types.severity_trends_count

        out["severity_trends"] = (
            aws_sdk_securityhub.types.severity_trends_count.deserialize_json(
                data["SeverityTrends"]
            )
        )
    return out
