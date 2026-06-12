"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentHashType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentHashType: TypeAlias = Literal[
    "Sha256",
    "Sha1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Sha256",
        "Sha1",
    )
)


def serialize_aws_json_1_1(value: DocumentHashType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentHashType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentHashType value: {data!r}")
    return cast(DocumentHashType, data)
