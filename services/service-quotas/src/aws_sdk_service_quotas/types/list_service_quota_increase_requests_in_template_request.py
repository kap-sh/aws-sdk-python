"""Generated from Smithy shape ``com.amazonaws.servicequotas#ListServiceQuotaIncreaseRequestsInTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.aws_region
    import aws_sdk_service_quotas.types.max_results
    import aws_sdk_service_quotas.types.next_token
    import aws_sdk_service_quotas.types.service_code


class ListServiceQuotaIncreaseRequestsInTemplateRequest(TypedDict):
    service_code: NotRequired["aws_sdk_service_quotas.types.service_code.ServiceCode"]
    """<p>Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the <a>ListServices</a> operation.</p>"""
    aws_region: NotRequired["aws_sdk_service_quotas.types.aws_region.AwsRegion"]
    """<p>Specifies the Amazon Web Services Region for which you made the request.</p>"""
    next_token: NotRequired["aws_sdk_service_quotas.types.next_token.NextToken"]
    """<p>Specifies a value for receiving additional results after you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["aws_sdk_service_quotas.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListServiceQuotaIncreaseRequestsInTemplateRequest,
) -> dict:
    out: dict = {}
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListServiceQuotaIncreaseRequestsInTemplateRequest:
    out: ListServiceQuotaIncreaseRequestsInTemplateRequest = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
