"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

LocationUpdateStatus: TypeAlias = Literal["PENDING_UPDATE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PENDING_UPDATE",))


def serialize_aws_json_1_1(value: LocationUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocationUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocationUpdateStatus value: {data!r}")
    return cast(LocationUpdateStatus, data)
