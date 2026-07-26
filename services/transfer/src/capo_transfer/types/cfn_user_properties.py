"""Generated from Smithy shape ``com.amazonaws.necco.coral#CfnUserProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.cfn_ssh_public_keys


class CfnUserProperties(TypedDict, closed=True):
    ssh_public_keys: NotRequired[
        "capo_transfer.types.cfn_ssh_public_keys.CfnSshPublicKeys"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnUserProperties) -> dict:
    out: dict = {}
    if "ssh_public_keys" in value:
        import capo_transfer.types.cfn_ssh_public_keys

        out["SshPublicKeys"] = (
            capo_transfer.types.cfn_ssh_public_keys.serialize_aws_json_1_1(
                value["ssh_public_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CfnUserProperties:
    out: CfnUserProperties = {}  # type: ignore[typeddict-item]
    if "SshPublicKeys" in data:
        import capo_transfer.types.cfn_ssh_public_keys

        out["ssh_public_keys"] = (
            capo_transfer.types.cfn_ssh_public_keys.deserialize_aws_json_1_1(
                data["SshPublicKeys"]
            )
        )
    return out
