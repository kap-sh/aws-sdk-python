"""Generated from Smithy shape ``com.amazonaws.acmpca#ListCertificateAuthoritiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.max_results
    import aws_sdk_acm_pca.types.next_token
    import aws_sdk_acm_pca.types.resource_owner


class ListCertificateAuthoritiesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_acm_pca.types.max_results.MaxResults"]
    """<p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p> <p>Although the maximum value is 1000, the action only returns a maximum of 100 items.</p>"""
    next_token: NotRequired["aws_sdk_acm_pca.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""
    resource_owner: NotRequired["aws_sdk_acm_pca.types.resource_owner.ResourceOwner"]
    """<p>Use this parameter to filter the returned set of certificate authorities based on their owner. The default is SELF.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificateAuthoritiesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_owner" in value:
        import aws_sdk_acm_pca.types.resource_owner

        out["ResourceOwner"] = (
            aws_sdk_acm_pca.types.resource_owner.serialize_aws_json_1_1(
                value["resource_owner"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificateAuthoritiesRequest:
    out: ListCertificateAuthoritiesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ResourceOwner" in data:
        import aws_sdk_acm_pca.types.resource_owner

        out["resource_owner"] = (
            aws_sdk_acm_pca.types.resource_owner.deserialize_aws_json_1_1(
                data["ResourceOwner"]
            )
        )
    return out
