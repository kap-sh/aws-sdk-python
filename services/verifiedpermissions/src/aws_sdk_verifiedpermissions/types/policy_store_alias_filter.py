"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyStoreAliasFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_id


class PolicyStoreAliasFilter(TypedDict):
    policy_store_id: NotRequired[
        "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    ]
    """<p>The ID of the policy store to filter by. Only policy store aliases associated with this policy store are returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStoreAliasFilter) -> dict:
    out: dict = {}
    if "policy_store_id" in value:
        out["policyStoreId"] = value["policy_store_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyStoreAliasFilter:
    out: PolicyStoreAliasFilter = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    return out
