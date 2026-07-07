"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEnrollmentStatusesForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.enrollment_filters
    import aws_sdk_compute_optimizer.types.max_results
    import aws_sdk_compute_optimizer.types.next_token


class GetEnrollmentStatusesForOrganizationRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_compute_optimizer.types.enrollment_filters.EnrollmentFilters"
    ]
    """<p>An array of objects to specify a filter that returns a more specific list of account enrollment statuses.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of account enrollment statuses.</p>"""
    max_results: NotRequired["aws_sdk_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of account enrollment statuses to return with a single request. You can specify up to 100 statuses to return with each request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentStatusesForOrganizationRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_compute_optimizer.types.enrollment_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.enrollment_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentStatusesForOrganizationRequest:
    out: GetEnrollmentStatusesForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_compute_optimizer.types.enrollment_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.enrollment_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
