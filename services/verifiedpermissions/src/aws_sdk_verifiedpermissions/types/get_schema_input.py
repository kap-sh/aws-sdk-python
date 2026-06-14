"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetSchemaInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_store_id


class GetSchemaInput(TypedDict):
    policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    r"""<p>Specifies the ID of the policy store that contains the schema.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html\">ListPolicyStoreAliases</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSchemaInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSchemaInput:
    out: GetSchemaInput = {}  # type: ignore[typeddict-item]
    if "policyStoreId" in data:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetSchemaInput.policy_store_id required")
    return out
