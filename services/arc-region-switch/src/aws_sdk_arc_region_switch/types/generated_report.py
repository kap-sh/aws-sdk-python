"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GeneratedReport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_arc_region_switch.types.report_output


class GeneratedReport(TypedDict):
    report_generation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the report was generated.</p>"""
    report_output: NotRequired[
        "aws_sdk_arc_region_switch.types.report_output.ReportOutput"
    ]
    """<p>The output location or cause of a failure in report generation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GeneratedReport) -> dict:
    out: dict = {}
    if "report_generation_time" in value:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["reportGenerationTime"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["report_generation_time"]
            )
        )
    if "report_output" in value:
        import aws_sdk_arc_region_switch.types.report_output

        out["reportOutput"] = (
            aws_sdk_arc_region_switch.types.report_output.serialize_aws_json_1_0(
                value["report_output"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GeneratedReport:
    out: GeneratedReport = {}  # type: ignore[typeddict-item]
    if "reportGenerationTime" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["report_generation_time"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["reportGenerationTime"]
            )
        )
    if "reportOutput" in data:
        import aws_sdk_arc_region_switch.types.report_output

        out["report_output"] = (
            aws_sdk_arc_region_switch.types.report_output.deserialize_aws_json_1_0(
                data["reportOutput"]
            )
        )
    return out
