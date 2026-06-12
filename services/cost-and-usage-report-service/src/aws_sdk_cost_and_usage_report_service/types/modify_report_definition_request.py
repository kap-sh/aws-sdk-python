"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ModifyReportDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.report_definition
    import aws_sdk_cost_and_usage_report_service.types.report_name


class ModifyReportDefinitionRequest(TypedDict):
    report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName"
    report_definition: (
        "aws_sdk_cost_and_usage_report_service.types.report_definition.ReportDefinition"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReportDefinitionRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import aws_sdk_cost_and_usage_report_service.types.report_definition

    out["ReportDefinition"] = (
        aws_sdk_cost_and_usage_report_service.types.report_definition.serialize_aws_json_1_1(
            value["report_definition"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReportDefinitionRequest:
    out: ModifyReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    else:
        raise DeserializationError("ModifyReportDefinitionRequest.report_name required")
    if "ReportDefinition" in data:
        import aws_sdk_cost_and_usage_report_service.types.report_definition

        out["report_definition"] = (
            aws_sdk_cost_and_usage_report_service.types.report_definition.deserialize_aws_json_1_1(
                data["ReportDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyReportDefinitionRequest.report_definition required"
        )
    return out
