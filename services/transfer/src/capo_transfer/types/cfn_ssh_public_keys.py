"""Generated from Smithy shape ``com.amazonaws.necco.coral#CfnSshPublicKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.ssh_public_key_body

CfnSshPublicKeys: TypeAlias = list[
    "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnSshPublicKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CfnSshPublicKeys:
    return list(data)
