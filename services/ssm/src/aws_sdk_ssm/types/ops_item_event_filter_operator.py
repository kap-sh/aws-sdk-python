"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemEventFilterOperator: TypeAlias = Literal["Equal",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Equal",))


def serialize_aws_json_1_1(value: OpsItemEventFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemEventFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpsItemEventFilterOperator value: {data!r}"
        )
    return cast(OpsItemEventFilterOperator, data)
