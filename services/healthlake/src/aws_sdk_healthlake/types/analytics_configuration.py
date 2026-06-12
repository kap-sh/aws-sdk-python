"""Generated from Smithy shape ``com.amazonaws.healthlake#AnalyticsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.analytics_status


class AnalyticsConfiguration(TypedDict):
    status: NotRequired["aws_sdk_healthlake.types.analytics_status.AnalyticsStatus"]
    """<para>The status of the analytics configuration.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalyticsConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_healthlake.types.analytics_status

        out["Status"] = (
            aws_sdk_healthlake.types.analytics_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AnalyticsConfiguration:
    out: AnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_healthlake.types.analytics_status

        out["status"] = (
            aws_sdk_healthlake.types.analytics_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
