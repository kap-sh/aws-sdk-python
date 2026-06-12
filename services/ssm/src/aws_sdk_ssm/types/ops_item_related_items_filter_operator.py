"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemRelatedItemsFilterOperator: TypeAlias = Literal["Equal",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Equal",))


def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemRelatedItemsFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpsItemRelatedItemsFilterOperator value: {data!r}"
        )
    return cast(OpsItemRelatedItemsFilterOperator, data)
