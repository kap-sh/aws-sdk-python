"""Generated from Smithy shape ``com.amazonaws.inspector#ListAssessmentTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_template_filter
    import capo_inspector.types.list_max_results
    import capo_inspector.types.list_parent_arn_list
    import capo_inspector.types.pagination_token


class ListAssessmentTemplatesRequest(TypedDict, closed=True):
    assessment_target_arns: NotRequired[
        "capo_inspector.types.list_parent_arn_list.ListParentArnList"
    ]
    """<p>A list of ARNs that specifies the assessment targets whose assessment templates you want to list.</p>"""
    filter: NotRequired[
        "capo_inspector.types.assessment_template_filter.AssessmentTemplateFilter"
    ]
    """<p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListAssessmentTemplates</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>"""
    max_results: NotRequired["capo_inspector.types.list_max_results.ListMaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssessmentTemplatesRequest) -> dict:
    out: dict = {}
    if "assessment_target_arns" in value:
        import capo_inspector.types.list_parent_arn_list

        out["assessmentTargetArns"] = (
            capo_inspector.types.list_parent_arn_list.serialize_aws_json_1_1(
                value["assessment_target_arns"]
            )
        )
    if "filter" in value:
        import capo_inspector.types.assessment_template_filter

        out["filter"] = (
            capo_inspector.types.assessment_template_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssessmentTemplatesRequest:
    out: ListAssessmentTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTargetArns" in data:
        import capo_inspector.types.list_parent_arn_list

        out["assessment_target_arns"] = (
            capo_inspector.types.list_parent_arn_list.deserialize_aws_json_1_1(
                data["assessmentTargetArns"]
            )
        )
    if "filter" in data:
        import capo_inspector.types.assessment_template_filter

        out["filter"] = (
            capo_inspector.types.assessment_template_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
