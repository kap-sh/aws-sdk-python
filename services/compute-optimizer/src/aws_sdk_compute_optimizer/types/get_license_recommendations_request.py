"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetLicenseRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_ids
    import aws_sdk_compute_optimizer.types.license_recommendation_filters
    import aws_sdk_compute_optimizer.types.max_results
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.resource_arns


class GetLicenseRecommendationsRequest(TypedDict):
    resource_arns: NotRequired[
        "aws_sdk_compute_optimizer.types.resource_arns.ResourceArns"
    ]
    """<p> The ARN that identifies the Amazon EC2 instance. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:ec2:region:aws_account_id:instance/instance-id</code> </p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to advance to the next page of license recommendations. </p>"""
    max_results: NotRequired["aws_sdk_compute_optimizer.types.max_results.MaxResults"]
    """<p> The maximum number of license recommendations to return with a single request. </p> <p> To retrieve the remaining results, make another request with the returned <code>nextToken</code> value. </p>"""
    filters: NotRequired[
        "aws_sdk_compute_optimizer.types.license_recommendation_filters.LicenseRecommendationFilters"
    ]
    """<p> An array of objects to specify a filter that returns a more specific list of license recommendations. </p>"""
    account_ids: NotRequired["aws_sdk_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The ID of the Amazon Web Services account for which to return license recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return license recommendations.</p> <p>Only one account ID can be specified per request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLicenseRecommendationsRequest) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import aws_sdk_compute_optimizer.types.resource_arns

        out["resourceArns"] = (
            aws_sdk_compute_optimizer.types.resource_arns.serialize_aws_json_1_0(
                value["resource_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_compute_optimizer.types.license_recommendation_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.license_recommendation_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_compute_optimizer.types.account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetLicenseRecommendationsRequest:
    out: GetLicenseRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "resourceArns" in data:
        import aws_sdk_compute_optimizer.types.resource_arns

        out["resource_arns"] = (
            aws_sdk_compute_optimizer.types.resource_arns.deserialize_aws_json_1_0(
                data["resourceArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_compute_optimizer.types.license_recommendation_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.license_recommendation_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "accountIds" in data:
        import aws_sdk_compute_optimizer.types.account_ids

        out["account_ids"] = (
            aws_sdk_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    return out
