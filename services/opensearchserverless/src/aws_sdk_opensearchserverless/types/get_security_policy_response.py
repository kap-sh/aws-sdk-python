"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetSecurityPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.security_policy_detail


class GetSecurityPolicyResponse(TypedDict, closed=True):
    security_policy_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.security_policy_detail.SecurityPolicyDetail"
    ]
    """<p>Details about the requested security policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSecurityPolicyResponse) -> dict:
    out: dict = {}
    if "security_policy_detail" in value:
        import aws_sdk_opensearchserverless.types.security_policy_detail

        out["securityPolicyDetail"] = (
            aws_sdk_opensearchserverless.types.security_policy_detail.serialize_aws_json_1_0(
                value["security_policy_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSecurityPolicyResponse:
    out: GetSecurityPolicyResponse = {}  # type: ignore[typeddict-item]
    if "securityPolicyDetail" in data:
        import aws_sdk_opensearchserverless.types.security_policy_detail

        out["security_policy_detail"] = (
            aws_sdk_opensearchserverless.types.security_policy_detail.deserialize_aws_json_1_0(
                data["securityPolicyDetail"]
            )
        )
    return out
