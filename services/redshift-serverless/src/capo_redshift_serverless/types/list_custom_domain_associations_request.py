"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListCustomDomainAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.pagination_token


class ListCustomDomainAssociationsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>"""
    custom_domain_name: NotRequired[
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    ]
    """<p>The custom domain name associated with the workgroup.</p>"""
    custom_domain_certificate_arn: NotRequired[
        "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The custom domain name’s certificate Amazon resource name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomDomainAssociationsRequest) -> dict:
    out: dict = {}
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "custom_domain_certificate_arn" in value:
        out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomDomainAssociationsRequest:
    out: ListCustomDomainAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "customDomainCertificateArn" in data:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    return out
