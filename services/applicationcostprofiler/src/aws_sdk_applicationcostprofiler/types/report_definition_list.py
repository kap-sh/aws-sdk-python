"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ReportDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.report_definition

ReportDefinitionList: TypeAlias = list[
    "aws_sdk_applicationcostprofiler.types.report_definition.ReportDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportDefinitionList) -> list:
    import aws_sdk_applicationcostprofiler.types.report_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_applicationcostprofiler.types.report_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReportDefinitionList:
    import aws_sdk_applicationcostprofiler.types.report_definition

    out: ReportDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_applicationcostprofiler.types.report_definition.deserialize_json(
                item
            )
        )
    return out
