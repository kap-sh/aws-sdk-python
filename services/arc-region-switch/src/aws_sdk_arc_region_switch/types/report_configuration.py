"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ReportConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.report_output_list


class ReportConfiguration(TypedDict):
    report_output: NotRequired[
        "aws_sdk_arc_region_switch.types.report_output_list.ReportOutputList"
    ]
    """<p>The output configuration for the report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportConfiguration) -> dict:
    out: dict = {}
    if "report_output" in value:
        import aws_sdk_arc_region_switch.types.report_output_list

        out["reportOutput"] = (
            aws_sdk_arc_region_switch.types.report_output_list.serialize_aws_json_1_0(
                value["report_output"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReportConfiguration:
    out: ReportConfiguration = {}  # type: ignore[typeddict-item]
    if "reportOutput" in data:
        import aws_sdk_arc_region_switch.types.report_output_list

        out["report_output"] = (
            aws_sdk_arc_region_switch.types.report_output_list.deserialize_aws_json_1_0(
                data["reportOutput"]
            )
        )
    return out
