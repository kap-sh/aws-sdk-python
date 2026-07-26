"""Generated from Smithy shape ``com.amazonaws.transfer#SshPublicKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.ssh_public_key

SshPublicKeys: TypeAlias = list["capo_transfer.types.ssh_public_key.SshPublicKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SshPublicKeys) -> list:
    import capo_transfer.types.ssh_public_key

    out: list = []
    for item in value:
        out.append(capo_transfer.types.ssh_public_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SshPublicKeys:
    import capo_transfer.types.ssh_public_key

    out: SshPublicKeys = []
    for item in data:
        out.append(capo_transfer.types.ssh_public_key.deserialize_aws_json_1_1(item))
    return out
