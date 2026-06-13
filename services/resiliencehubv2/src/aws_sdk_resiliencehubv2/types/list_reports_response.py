"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListReportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.report_generation_result_list


class ListReportsResponse(TypedDict):
    report_generation_results: "aws_sdk_resiliencehubv2.types.report_generation_result_list.ReportGenerationResultList"
    """<p>The list of report generation results.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReportsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.report_generation_result_list

    out["reportGenerationResults"] = (
        aws_sdk_resiliencehubv2.types.report_generation_result_list.serialize_json(
            value["report_generation_results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportsResponse:
    out: ListReportsResponse = {}  # type: ignore[typeddict-item]
    if "reportGenerationResults" in data:
        import aws_sdk_resiliencehubv2.types.report_generation_result_list

        out["report_generation_results"] = (
            aws_sdk_resiliencehubv2.types.report_generation_result_list.deserialize_json(
                data["reportGenerationResults"]
            )
        )
    else:
        raise DeserializationError(
            "ListReportsResponse.report_generation_results required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
