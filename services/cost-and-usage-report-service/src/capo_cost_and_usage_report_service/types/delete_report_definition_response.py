"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DeleteReportDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.delete_response_message


class DeleteReportDefinitionResponse(TypedDict, closed=True):
    response_message: NotRequired[
        "capo_cost_and_usage_report_service.types.delete_response_message.DeleteResponseMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportDefinitionResponse) -> dict:
    out: dict = {}
    if "response_message" in value:
        out["ResponseMessage"] = value["response_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportDefinitionResponse:
    out: DeleteReportDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "ResponseMessage" in data:
        out["response_message"] = data["ResponseMessage"]
    return out
