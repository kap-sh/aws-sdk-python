"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListSecurityConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.security_config_summaries


class ListSecurityConfigsResponse(TypedDict):
    security_config_summaries: NotRequired[
        "aws_sdk_opensearchserverless.types.security_config_summaries.SecurityConfigSummaries"
    ]
    """<p>Details about the security configurations in your account.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSecurityConfigsResponse) -> dict:
    out: dict = {}
    if "security_config_summaries" in value:
        import aws_sdk_opensearchserverless.types.security_config_summaries

        out["securityConfigSummaries"] = (
            aws_sdk_opensearchserverless.types.security_config_summaries.serialize_aws_json_1_0(
                value["security_config_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSecurityConfigsResponse:
    out: ListSecurityConfigsResponse = {}  # type: ignore[typeddict-item]
    if "securityConfigSummaries" in data:
        import aws_sdk_opensearchserverless.types.security_config_summaries

        out["security_config_summaries"] = (
            aws_sdk_opensearchserverless.types.security_config_summaries.deserialize_aws_json_1_0(
                data["securityConfigSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
