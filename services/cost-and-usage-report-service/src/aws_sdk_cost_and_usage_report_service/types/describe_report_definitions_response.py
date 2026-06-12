"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DescribeReportDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.generic_string
    import aws_sdk_cost_and_usage_report_service.types.report_definition_list


class DescribeReportDefinitionsResponse(TypedDict):
    report_definitions: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.report_definition_list.ReportDefinitionList"
    ]
    """<p>An Amazon Web Services Cost and Usage Report list owned by the account.</p>"""
    next_token: NotRequired[
        "aws_sdk_cost_and_usage_report_service.types.generic_string.GenericString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReportDefinitionsResponse) -> dict:
    out: dict = {}
    if "report_definitions" in value:
        import aws_sdk_cost_and_usage_report_service.types.report_definition_list

        out["ReportDefinitions"] = (
            aws_sdk_cost_and_usage_report_service.types.report_definition_list.serialize_aws_json_1_1(
                value["report_definitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReportDefinitionsResponse:
    out: DescribeReportDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "ReportDefinitions" in data:
        import aws_sdk_cost_and_usage_report_service.types.report_definition_list

        out["report_definitions"] = (
            aws_sdk_cost_and_usage_report_service.types.report_definition_list.deserialize_aws_json_1_1(
                data["ReportDefinitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
