"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetAccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.access_policy_detail


class GetAccessPolicyResponse(TypedDict, closed=True):
    access_policy_detail: NotRequired[
        "capo_opensearchserverless.types.access_policy_detail.AccessPolicyDetail"
    ]
    """<p>Details about the requested access policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccessPolicyResponse) -> dict:
    out: dict = {}
    if "access_policy_detail" in value:
        import capo_opensearchserverless.types.access_policy_detail

        out["accessPolicyDetail"] = (
            capo_opensearchserverless.types.access_policy_detail.serialize_aws_json_1_0(
                value["access_policy_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccessPolicyResponse:
    out: GetAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if "accessPolicyDetail" in data:
        import capo_opensearchserverless.types.access_policy_detail

        out["access_policy_detail"] = (
            capo_opensearchserverless.types.access_policy_detail.deserialize_aws_json_1_0(
                data["accessPolicyDetail"]
            )
        )
    return out
