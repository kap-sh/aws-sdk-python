"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportFrequency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.integer
    import aws_sdk_license_manager.types.report_frequency_type


class ReportFrequency(TypedDict):
    value: NotRequired["aws_sdk_license_manager.types.integer.Integer"]
    """<p>Number of times within the frequency period that a report is generated. The only supported value is <code>1</code>.</p>"""
    period: NotRequired[
        "aws_sdk_license_manager.types.report_frequency_type.ReportFrequencyType"
    ]
    """<p>Time period between each report. The period can be daily, weekly, or monthly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFrequency) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "period" in value:
        import aws_sdk_license_manager.types.report_frequency_type

        out["period"] = (
            aws_sdk_license_manager.types.report_frequency_type.serialize_aws_json_1_1(
                value["period"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportFrequency:
    out: ReportFrequency = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "period" in data:
        import aws_sdk_license_manager.types.report_frequency_type

        out["period"] = (
            aws_sdk_license_manager.types.report_frequency_type.deserialize_aws_json_1_1(
                data["period"]
            )
        )
    return out
