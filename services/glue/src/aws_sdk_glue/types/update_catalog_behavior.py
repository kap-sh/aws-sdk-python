"""Generated from Smithy shape ``com.amazonaws.glue#UpdateCatalogBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

UpdateCatalogBehavior: TypeAlias = Literal[
    "UPDATE_IN_DATABASE",
    "LOG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATE_IN_DATABASE",
        "LOG",
    )
)


def serialize_aws_json_1_1(value: UpdateCatalogBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateCatalogBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateCatalogBehavior value: {data!r}")
    return cast(UpdateCatalogBehavior, data)
