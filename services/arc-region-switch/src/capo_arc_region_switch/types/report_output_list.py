"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ReportOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.report_output_configuration

ReportOutputList: TypeAlias = list[
    "capo_arc_region_switch.types.report_output_configuration.ReportOutputConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReportOutputList) -> list:
    import capo_arc_region_switch.types.report_output_configuration

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.report_output_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReportOutputList:
    import capo_arc_region_switch.types.report_output_configuration

    out: ReportOutputList = []
    for item in data:
        out.append(
            capo_arc_region_switch.types.report_output_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out
