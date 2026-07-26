"""Generated from Smithy shape ``com.amazonaws.s3control#ScopePermission``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

ScopePermission: TypeAlias = Literal[
    "GetObject",
    "GetObjectAttributes",
    "ListMultipartUploadParts",
    "ListBucket",
    "ListBucketMultipartUploads",
    "PutObject",
    "DeleteObject",
    "AbortMultipartUpload",
]


# --- restXml ser/de ---
def to_xml_text(value: ScopePermission) -> str:
    return value


def from_xml_text(text: str) -> ScopePermission:
    return cast(ScopePermission, text)


def serialize_xml(value: ScopePermission, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ScopePermission:
    return from_xml_text(el.text or "")
