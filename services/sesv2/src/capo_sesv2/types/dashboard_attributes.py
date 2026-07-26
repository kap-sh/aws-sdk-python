"""Generated from Smithy shape ``com.amazonaws.sesv2#DashboardAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.feature_status


class DashboardAttributes(TypedDict, closed=True):
    engagement_metrics: NotRequired["capo_sesv2.types.feature_status.FeatureStatus"]
    """<p>Specifies the status of your VDM engagement metrics collection. Can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Amazon SES enables engagement metrics for your account.</p> </li> <li> <p> <code>DISABLED</code> – Amazon SES disables engagement metrics for your account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardAttributes) -> dict:
    out: dict = {}
    if "engagement_metrics" in value:
        import capo_sesv2.types.feature_status

        out["EngagementMetrics"] = capo_sesv2.types.feature_status.serialize_json(
            value["engagement_metrics"]
        )
    return out


def deserialize_json(data: dict) -> DashboardAttributes:
    out: DashboardAttributes = {}  # type: ignore[typeddict-item]
    if "EngagementMetrics" in data:
        import capo_sesv2.types.feature_status

        out["engagement_metrics"] = capo_sesv2.types.feature_status.deserialize_json(
            data["EngagementMetrics"]
        )
    return out
