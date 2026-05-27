"""Generated from Smithy shape ``com.amazonaws.s3#InventoryOptionalField``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

InventoryOptionalField: TypeAlias = Literal[
    "Size",
    "LastModifiedDate",
    "StorageClass",
    "ETag",
    "IsMultipartUploaded",
    "ReplicationStatus",
    "EncryptionStatus",
    "ObjectLockRetainUntilDate",
    "ObjectLockMode",
    "ObjectLockLegalHoldStatus",
    "IntelligentTieringAccessTier",
    "BucketKeyStatus",
    "ChecksumAlgorithm",
    "ObjectAccessControlList",
    "ObjectOwner",
    "LifecycleExpirationDate",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Size",
        "LastModifiedDate",
        "StorageClass",
        "ETag",
        "IsMultipartUploaded",
        "ReplicationStatus",
        "EncryptionStatus",
        "ObjectLockRetainUntilDate",
        "ObjectLockMode",
        "ObjectLockLegalHoldStatus",
        "IntelligentTieringAccessTier",
        "BucketKeyStatus",
        "ChecksumAlgorithm",
        "ObjectAccessControlList",
        "ObjectOwner",
        "LifecycleExpirationDate",
    )
)


def to_xml_text(value: InventoryOptionalField) -> str:
    return value


def from_xml_text(text: str) -> InventoryOptionalField:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InventoryOptionalField value: {text!r}")
    return cast(InventoryOptionalField, text)


def serialize_xml(value: InventoryOptionalField, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> InventoryOptionalField:
    return from_xml_text(el.text or "")
