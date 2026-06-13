"""Generated from Smithy shape ``com.amazonaws.evs#EntitlementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_evs.errors import DeserializationError

EntitlementType: TypeAlias = Literal["WINDOWS_SERVER",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("WINDOWS_SERVER",))


def serialize_aws_json_1_0(value: EntitlementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EntitlementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntitlementType value: {data!r}")
    return cast(EntitlementType, data)
