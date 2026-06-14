"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyStoreAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.alias


class GetPolicyStoreAliasInput(TypedDict):
    alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias"
    """<p>Specifies the name of the policy store alias that you want information about.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyStoreAliasInput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyStoreAliasInput:
    out: GetPolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
    if "aliasName" in data:
        out["alias_name"] = data["aliasName"]
    else:
        raise DeserializationError("GetPolicyStoreAliasInput.alias_name required")
    return out
