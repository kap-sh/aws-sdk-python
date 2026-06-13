"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressPointStatus: TypeAlias = Literal[
    "PROVISIONING",
    "DEPROVISIONING",
    "UPDATING",
    "ACTIVE",
    "CLOSED",
    "FAILED",
    "ASSOCIATED_VPC_ENDPOINT_DOES_NOT_EXIST",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "DEPROVISIONING",
        "UPDATING",
        "ACTIVE",
        "CLOSED",
        "FAILED",
        "ASSOCIATED_VPC_ENDPOINT_DOES_NOT_EXIST",
    )
)


def serialize_aws_json_1_0(value: IngressPointStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressPointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressPointStatus value: {data!r}")
    return cast(IngressPointStatus, data)
