"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.domain_list
    import aws_sdk_sagemaker.types.next_token


class ListDomainsResponse(TypedDict, closed=True):
    domains: NotRequired["aws_sdk_sagemaker.types.domain_list.DomainList"]
    """<p>The list of domains.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDomainsResponse) -> dict:
    out: dict = {}
    if "domains" in value:
        import aws_sdk_sagemaker.types.domain_list

        out["Domains"] = aws_sdk_sagemaker.types.domain_list.serialize_aws_json_1_1(
            value["domains"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if "Domains" in data:
        import aws_sdk_sagemaker.types.domain_list

        out["domains"] = aws_sdk_sagemaker.types.domain_list.deserialize_aws_json_1_1(
            data["Domains"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
