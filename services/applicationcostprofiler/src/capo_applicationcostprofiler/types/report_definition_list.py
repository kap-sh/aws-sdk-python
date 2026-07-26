"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ReportDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.report_definition

ReportDefinitionList: TypeAlias = list[
    "capo_applicationcostprofiler.types.report_definition.ReportDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportDefinitionList) -> list:
    import capo_applicationcostprofiler.types.report_definition

    out: list = []
    for item in value:
        out.append(
            capo_applicationcostprofiler.types.report_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReportDefinitionList:
    import capo_applicationcostprofiler.types.report_definition

    out: ReportDefinitionList = []
    for item in data:
        out.append(
            capo_applicationcostprofiler.types.report_definition.deserialize_json(item)
        )
    return out
