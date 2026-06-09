"""Generated from Smithy shape ``com.amazonaws.iam#SSHPublicKeyListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.ssh_public_key_metadata

SSHPublicKeyListType: TypeAlias = list[
    "aws_sdk_iam.types.ssh_public_key_metadata.SSHPublicKeyMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SSHPublicKeyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.ssh_public_key_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.ssh_public_key_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SSHPublicKeyListType:
    import aws_sdk_iam.types.ssh_public_key_metadata

    out: SSHPublicKeyListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.ssh_public_key_metadata.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SSHPublicKeyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.ssh_public_key_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.ssh_public_key_metadata.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SSHPublicKeyListType:
    import aws_sdk_iam.types.ssh_public_key_metadata

    out: SSHPublicKeyListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.ssh_public_key_metadata.deserialize_query(child))
    return out
