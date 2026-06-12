"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListResponseScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

ListResponseScope: TypeAlias = Literal["METADATA_ONLY",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("METADATA_ONLY",))


def serialize_aws_json_1_0(value: ListResponseScope) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListResponseScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListResponseScope value: {data!r}")
    return cast(ListResponseScope, data)
