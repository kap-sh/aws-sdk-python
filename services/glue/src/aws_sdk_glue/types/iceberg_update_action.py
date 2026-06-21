"""Generated from Smithy shape ``com.amazonaws.glue#IcebergUpdateAction``."""

from typing import Literal, TypeAlias, cast

IcebergUpdateAction: TypeAlias = Literal[
    "add-schema",
    "set-current-schema",
    "add-spec",
    "set-default-spec",
    "add-sort-order",
    "set-default-sort-order",
    "set-location",
    "set-properties",
    "remove-properties",
    "add-encryption-key",
    "remove-encryption-key",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergUpdateAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergUpdateAction:
    return cast(IcebergUpdateAction, data)
