"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransferType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

ResponsibilityTransferType: TypeAlias = Literal["BILLING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BILLING",))


def serialize_aws_json_1_1(value: ResponsibilityTransferType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResponsibilityTransferType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResponsibilityTransferType value: {data!r}"
        )
    return cast(ResponsibilityTransferType, data)
