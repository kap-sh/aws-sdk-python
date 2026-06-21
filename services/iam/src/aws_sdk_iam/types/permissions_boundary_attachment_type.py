"""Generated from Smithy shape ``com.amazonaws.iam#PermissionsBoundaryAttachmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

PermissionsBoundaryAttachmentType: TypeAlias = Literal["PermissionsBoundaryPolicy",]


# --- awsQuery ser/de ---
def to_query_text(value: PermissionsBoundaryAttachmentType) -> str:
    return value


def from_query_text(text: str) -> PermissionsBoundaryAttachmentType:
    return cast(PermissionsBoundaryAttachmentType, text)


def serialize_query(
    value: PermissionsBoundaryAttachmentType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PermissionsBoundaryAttachmentType:
    return from_query_text(el.text or "")
