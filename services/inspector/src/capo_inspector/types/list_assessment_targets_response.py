"""Generated from Smithy shape ``com.amazonaws.inspector#ListAssessmentTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.list_returned_arn_list
    import capo_inspector.types.pagination_token


class ListAssessmentTargetsResponse(TypedDict, closed=True):
    assessment_target_arns: (
        "capo_inspector.types.list_returned_arn_list.ListReturnedArnList"
    )
    """<p>A list of ARNs that specifies the assessment targets that are returned by the action.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssessmentTargetsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.list_returned_arn_list

    out["assessmentTargetArns"] = (
        capo_inspector.types.list_returned_arn_list.serialize_aws_json_1_1(
            value["assessment_target_arns"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssessmentTargetsResponse:
    out: ListAssessmentTargetsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentTargetArns" in data:
        import capo_inspector.types.list_returned_arn_list

        out["assessment_target_arns"] = (
            capo_inspector.types.list_returned_arn_list.deserialize_aws_json_1_1(
                data["assessmentTargetArns"]
            )
        )
    else:
        raise DeserializationError(
            "ListAssessmentTargetsResponse.assessment_target_arns required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
