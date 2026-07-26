"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ReportDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.report_definition

ReportDefinitionList: TypeAlias = list[
    "capo_cost_and_usage_report_service.types.report_definition.ReportDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportDefinitionList) -> list:
    import capo_cost_and_usage_report_service.types.report_definition

    out: list = []
    for item in value:
        out.append(
            capo_cost_and_usage_report_service.types.report_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReportDefinitionList:
    import capo_cost_and_usage_report_service.types.report_definition

    out: ReportDefinitionList = []
    for item in data:
        out.append(
            capo_cost_and_usage_report_service.types.report_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
