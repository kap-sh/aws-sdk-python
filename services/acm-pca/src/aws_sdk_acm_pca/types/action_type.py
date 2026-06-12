"""Generated from Smithy shape ``com.amazonaws.acmpca#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "IssueCertificate",
    "GetCertificate",
    "ListPermissions",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IssueCertificate",
        "GetCertificate",
        "ListPermissions",
    )
)


def serialize_aws_json_1_1(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
