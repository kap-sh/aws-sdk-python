"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransferStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

ResponsibilityTransferStatus: TypeAlias = Literal[
    "REQUESTED",
    "DECLINED",
    "CANCELED",
    "EXPIRED",
    "ACCEPTED",
    "WITHDRAWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "DECLINED",
        "CANCELED",
        "EXPIRED",
        "ACCEPTED",
        "WITHDRAWN",
    )
)


def serialize_aws_json_1_1(value: ResponsibilityTransferStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResponsibilityTransferStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResponsibilityTransferStatus value: {data!r}"
        )
    return cast(ResponsibilityTransferStatus, data)
