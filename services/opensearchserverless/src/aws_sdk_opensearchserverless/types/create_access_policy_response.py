"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateAccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.access_policy_detail


class CreateAccessPolicyResponse(TypedDict, closed=True):
    access_policy_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.access_policy_detail.AccessPolicyDetail"
    ]
    """<p>Details about the created access policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAccessPolicyResponse) -> dict:
    out: dict = {}
    if "access_policy_detail" in value:
        import aws_sdk_opensearchserverless.types.access_policy_detail

        out["accessPolicyDetail"] = (
            aws_sdk_opensearchserverless.types.access_policy_detail.serialize_aws_json_1_0(
                value["access_policy_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAccessPolicyResponse:
    out: CreateAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if "accessPolicyDetail" in data:
        import aws_sdk_opensearchserverless.types.access_policy_detail

        out["access_policy_detail"] = (
            aws_sdk_opensearchserverless.types.access_policy_detail.deserialize_aws_json_1_0(
                data["accessPolicyDetail"]
            )
        )
    return out
