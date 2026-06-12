"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#FileClassification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

FileClassification: TypeAlias = Literal[
    "MODELIZEIT_EXPORT",
    "RVTOOLS_EXPORT",
    "VMWARE_NSX_EXPORT",
    "IMPORT_TEMPLATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MODELIZEIT_EXPORT",
        "RVTOOLS_EXPORT",
        "VMWARE_NSX_EXPORT",
        "IMPORT_TEMPLATE",
    )
)


def serialize_aws_json_1_1(value: FileClassification) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileClassification:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileClassification value: {data!r}")
    return cast(FileClassification, data)
