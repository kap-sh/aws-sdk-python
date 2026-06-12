"""Generated from Smithy shape ``com.amazonaws.acmpca#AccessMethodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

AccessMethodType: TypeAlias = Literal[
    "CA_REPOSITORY",
    "RESOURCE_PKI_MANIFEST",
    "RESOURCE_PKI_NOTIFY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CA_REPOSITORY",
        "RESOURCE_PKI_MANIFEST",
        "RESOURCE_PKI_NOTIFY",
    )
)


def serialize_aws_json_1_1(value: AccessMethodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessMethodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessMethodType value: {data!r}")
    return cast(AccessMethodType, data)
