"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAccessScopesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.max_results
    import aws_sdk_sso_admin.types.token


class ListApplicationAccessScopesRequest(TypedDict):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application.</p>"""
    max_results: "aws_sdk_sso_admin.types.max_results.MaxResults"
    """<p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationAccessScopesRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["MaxResults"] = value.get("max_results", 10)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationAccessScopesRequest:
    out: ListApplicationAccessScopesRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "ListApplicationAccessScopesRequest.application_arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 10
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
