"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteriaAbortAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AwsJobAbortCriteriaAbortAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CANCEL",))


def serialize_json(value: AwsJobAbortCriteriaAbortAction) -> str:
    return value


def deserialize_json(data: str) -> AwsJobAbortCriteriaAbortAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AwsJobAbortCriteriaAbortAction value: {data!r}"
        )
    return cast(AwsJobAbortCriteriaAbortAction, data)
