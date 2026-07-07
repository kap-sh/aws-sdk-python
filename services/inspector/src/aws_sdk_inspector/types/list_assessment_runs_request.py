"""Generated from Smithy shape ``com.amazonaws.inspector#ListAssessmentRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_filter
    import aws_sdk_inspector.types.list_max_results
    import aws_sdk_inspector.types.list_parent_arn_list
    import aws_sdk_inspector.types.pagination_token


class ListAssessmentRunsRequest(TypedDict, closed=True):
    assessment_template_arns: NotRequired[
        "aws_sdk_inspector.types.list_parent_arn_list.ListParentArnList"
    ]
    """<p>The ARNs that specify the assessment templates whose assessment runs you want to list.</p>"""
    filter: NotRequired[
        "aws_sdk_inspector.types.assessment_run_filter.AssessmentRunFilter"
    ]
    """<p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListAssessmentRuns</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>"""
    max_results: NotRequired["aws_sdk_inspector.types.list_max_results.ListMaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssessmentRunsRequest) -> dict:
    out: dict = {}
    if "assessment_template_arns" in value:
        import aws_sdk_inspector.types.list_parent_arn_list

        out["assessmentTemplateArns"] = (
            aws_sdk_inspector.types.list_parent_arn_list.serialize_aws_json_1_1(
                value["assessment_template_arns"]
            )
        )
    if "filter" in value:
        import aws_sdk_inspector.types.assessment_run_filter

        out["filter"] = (
            aws_sdk_inspector.types.assessment_run_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssessmentRunsRequest:
    out: ListAssessmentRunsRequest = {}  # type: ignore[typeddict-item]
    if "assessmentTemplateArns" in data:
        import aws_sdk_inspector.types.list_parent_arn_list

        out["assessment_template_arns"] = (
            aws_sdk_inspector.types.list_parent_arn_list.deserialize_aws_json_1_1(
                data["assessmentTemplateArns"]
            )
        )
    if "filter" in data:
        import aws_sdk_inspector.types.assessment_run_filter

        out["filter"] = (
            aws_sdk_inspector.types.assessment_run_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
