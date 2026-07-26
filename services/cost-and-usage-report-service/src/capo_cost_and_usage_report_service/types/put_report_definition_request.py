"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#PutReportDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.report_definition
    import capo_cost_and_usage_report_service.types.tag_list


class PutReportDefinitionRequest(TypedDict, closed=True):
    report_definition: (
        "capo_cost_and_usage_report_service.types.report_definition.ReportDefinition"
    )
    """<p>Represents the output of the PutReportDefinition operation. The content consists of the detailed metadata and data file information. </p>"""
    tags: NotRequired["capo_cost_and_usage_report_service.types.tag_list.TagList"]
    """<p>The tags to be assigned to the report definition resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutReportDefinitionRequest) -> dict:
    out: dict = {}
    import capo_cost_and_usage_report_service.types.report_definition

    out["ReportDefinition"] = (
        capo_cost_and_usage_report_service.types.report_definition.serialize_aws_json_1_1(
            value["report_definition"]
        )
    )
    if "tags" in value:
        import capo_cost_and_usage_report_service.types.tag_list

        out["Tags"] = (
            capo_cost_and_usage_report_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutReportDefinitionRequest:
    out: PutReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "ReportDefinition" in data:
        import capo_cost_and_usage_report_service.types.report_definition

        out["report_definition"] = (
            capo_cost_and_usage_report_service.types.report_definition.deserialize_aws_json_1_1(
                data["ReportDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "PutReportDefinitionRequest.report_definition required"
        )
    if "Tags" in data:
        import capo_cost_and_usage_report_service.types.tag_list

        out["tags"] = (
            capo_cost_and_usage_report_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
