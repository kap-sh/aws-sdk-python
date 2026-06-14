"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPolicyStoresOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.next_token
    import aws_sdk_verifiedpermissions.types.policy_store_list


class ListPolicyStoresOutput(TypedDict):
    next_token: NotRequired["aws_sdk_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    policy_stores: "aws_sdk_verifiedpermissions.types.policy_store_list.PolicyStoreList"
    """<p>The list of policy stores in the account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPolicyStoresOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_verifiedpermissions.types.policy_store_list

    out["policyStores"] = (
        aws_sdk_verifiedpermissions.types.policy_store_list.serialize_aws_json_1_0(
            value["policy_stores"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPolicyStoresOutput:
    out: ListPolicyStoresOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "policyStores" in data:
        import aws_sdk_verifiedpermissions.types.policy_store_list

        out["policy_stores"] = (
            aws_sdk_verifiedpermissions.types.policy_store_list.deserialize_aws_json_1_0(
                data["policyStores"]
            )
        )
    else:
        raise DeserializationError("ListPolicyStoresOutput.policy_stores required")
    return out
