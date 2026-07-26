"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DescribeReportDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.generic_string
    import capo_cost_and_usage_report_service.types.report_definition_list


class DescribeReportDefinitionsResponse(TypedDict, closed=True):
    report_definitions: NotRequired[
        "capo_cost_and_usage_report_service.types.report_definition_list.ReportDefinitionList"
    ]
    """<p>An Amazon Web Services Cost and Usage Report list owned by the account.</p>"""
    next_token: NotRequired[
        "capo_cost_and_usage_report_service.types.generic_string.GenericString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReportDefinitionsResponse) -> dict:
    out: dict = {}
    if "report_definitions" in value:
        import capo_cost_and_usage_report_service.types.report_definition_list

        out["ReportDefinitions"] = (
            capo_cost_and_usage_report_service.types.report_definition_list.serialize_aws_json_1_1(
                value["report_definitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReportDefinitionsResponse:
    out: DescribeReportDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "ReportDefinitions" in data:
        import capo_cost_and_usage_report_service.types.report_definition_list

        out["report_definitions"] = (
            capo_cost_and_usage_report_service.types.report_definition_list.deserialize_aws_json_1_1(
                data["ReportDefinitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
