"""Generated from Smithy shape ``com.amazonaws.fsx#OntapFileSystemUserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OntapFileSystemUserType: TypeAlias = Literal[
    "UNIX",
    "WINDOWS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNIX",
        "WINDOWS",
    )
)


def serialize_aws_json_1_1(value: OntapFileSystemUserType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OntapFileSystemUserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OntapFileSystemUserType value: {data!r}")
    return cast(OntapFileSystemUserType, data)
