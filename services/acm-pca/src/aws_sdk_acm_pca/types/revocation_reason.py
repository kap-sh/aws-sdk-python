"""Generated from Smithy shape ``com.amazonaws.acmpca#RevocationReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

RevocationReason: TypeAlias = Literal[
    "UNSPECIFIED",
    "KEY_COMPROMISE",
    "CERTIFICATE_AUTHORITY_COMPROMISE",
    "AFFILIATION_CHANGED",
    "SUPERSEDED",
    "CESSATION_OF_OPERATION",
    "PRIVILEGE_WITHDRAWN",
    "A_A_COMPROMISE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNSPECIFIED",
        "KEY_COMPROMISE",
        "CERTIFICATE_AUTHORITY_COMPROMISE",
        "AFFILIATION_CHANGED",
        "SUPERSEDED",
        "CESSATION_OF_OPERATION",
        "PRIVILEGE_WITHDRAWN",
        "A_A_COMPROMISE",
    )
)


def serialize_aws_json_1_1(value: RevocationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RevocationReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RevocationReason value: {data!r}")
    return cast(RevocationReason, data)
