"""Generated from Smithy shape ``com.amazonaws.iot#ListSbomValidationResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.sbom_validation_result_summary_list


class ListSbomValidationResultsResponse(TypedDict, closed=True):
    validation_result_summaries: NotRequired[
        "aws_sdk_iot.types.sbom_validation_result_summary_list.SbomValidationResultSummaryList"
    ]
    """<p>A summary of the validation results for each software bill of materials attached to a software package version.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSbomValidationResultsResponse) -> dict:
    out: dict = {}
    if "validation_result_summaries" in value:
        import aws_sdk_iot.types.sbom_validation_result_summary_list

        out["validationResultSummaries"] = (
            aws_sdk_iot.types.sbom_validation_result_summary_list.serialize_json(
                value["validation_result_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSbomValidationResultsResponse:
    out: ListSbomValidationResultsResponse = {}  # type: ignore[typeddict-item]
    if "validationResultSummaries" in data:
        import aws_sdk_iot.types.sbom_validation_result_summary_list

        out["validation_result_summaries"] = (
            aws_sdk_iot.types.sbom_validation_result_summary_list.deserialize_json(
                data["validationResultSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
