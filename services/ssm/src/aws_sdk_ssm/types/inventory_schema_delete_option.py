"""Generated from Smithy shape ``com.amazonaws.ssm#InventorySchemaDeleteOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InventorySchemaDeleteOption: TypeAlias = Literal[
    "DisableSchema",
    "DeleteSchema",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DisableSchema",
        "DeleteSchema",
    )
)


def serialize_aws_json_1_1(value: InventorySchemaDeleteOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InventorySchemaDeleteOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InventorySchemaDeleteOption value: {data!r}"
        )
    return cast(InventorySchemaDeleteOption, data)
