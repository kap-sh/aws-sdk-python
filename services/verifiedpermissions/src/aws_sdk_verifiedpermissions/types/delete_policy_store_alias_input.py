"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletePolicyStoreAliasInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.alias
    import aws_sdk_verifiedpermissions.types.deletion_mode


class DeletePolicyStoreAliasInput(TypedDict):
    alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias"
    """<p>Specifies the name of the policy store alias that you want to delete.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>"""
    deletion_mode: NotRequired[
        "aws_sdk_verifiedpermissions.types.deletion_mode.DeletionMode"
    ]
    """<p>Specifies the deletion mode for the policy store alias. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The policy store alias enters the <code>PendingDeletion</code> state. This is the default behavior when no <code>deletionMode</code> is specified.</p> </li> <li> <p> <b>HardDelete</b> – The policy store alias is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePolicyStoreAliasInput) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    if "deletion_mode" in value:
        import aws_sdk_verifiedpermissions.types.deletion_mode

        out["deletionMode"] = (
            aws_sdk_verifiedpermissions.types.deletion_mode.serialize_aws_json_1_0(
                value["deletion_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePolicyStoreAliasInput:
    out: DeletePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
    if "aliasName" in data:
        out["alias_name"] = data["aliasName"]
    else:
        raise DeserializationError("DeletePolicyStoreAliasInput.alias_name required")
    if "deletionMode" in data:
        import aws_sdk_verifiedpermissions.types.deletion_mode

        out["deletion_mode"] = (
            aws_sdk_verifiedpermissions.types.deletion_mode.deserialize_aws_json_1_0(
                data["deletionMode"]
            )
        )
    return out
