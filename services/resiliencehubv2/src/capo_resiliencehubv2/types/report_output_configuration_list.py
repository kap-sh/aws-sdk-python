"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportOutputConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.report_output_configuration

ReportOutputConfigurationList: TypeAlias = list[
    "capo_resiliencehubv2.types.report_output_configuration.ReportOutputConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportOutputConfigurationList) -> list:
    import capo_resiliencehubv2.types.report_output_configuration

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.report_output_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReportOutputConfigurationList:
    import capo_resiliencehubv2.types.report_output_configuration

    out: ReportOutputConfigurationList = []
    for item in data:
        out.append(
            capo_resiliencehubv2.types.report_output_configuration.deserialize_json(
                item
            )
        )
    return out
