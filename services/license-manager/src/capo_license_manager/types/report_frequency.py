"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportFrequency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.integer
    import capo_license_manager.types.report_frequency_type


class ReportFrequency(TypedDict, closed=True):
    value: NotRequired["capo_license_manager.types.integer.Integer"]
    """<p>Number of times within the frequency period that a report is generated. The only supported value is <code>1</code>.</p>"""
    period: NotRequired[
        "capo_license_manager.types.report_frequency_type.ReportFrequencyType"
    ]
    """<p>Time period between each report. The period can be daily, weekly, or monthly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFrequency) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "period" in value:
        import capo_license_manager.types.report_frequency_type

        out["period"] = (
            capo_license_manager.types.report_frequency_type.serialize_aws_json_1_1(
                value["period"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportFrequency:
    out: ReportFrequency = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "period" in data:
        import capo_license_manager.types.report_frequency_type

        out["period"] = (
            capo_license_manager.types.report_frequency_type.deserialize_aws_json_1_1(
                data["period"]
            )
        )
    return out
