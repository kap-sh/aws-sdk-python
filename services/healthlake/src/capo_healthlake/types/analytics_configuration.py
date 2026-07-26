"""Generated from Smithy shape ``com.amazonaws.healthlake#AnalyticsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.analytics_status


class AnalyticsConfiguration(TypedDict, closed=True):
    status: NotRequired["capo_healthlake.types.analytics_status.AnalyticsStatus"]
    """<para>The status of the analytics configuration.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalyticsConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_healthlake.types.analytics_status

        out["Status"] = capo_healthlake.types.analytics_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AnalyticsConfiguration:
    out: AnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_healthlake.types.analytics_status

        out["status"] = capo_healthlake.types.analytics_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out
