"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobGenericDataSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

CodegenJobGenericDataSourceType: TypeAlias = Literal["DataStore",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DataStore",))


def serialize_json(value: CodegenJobGenericDataSourceType) -> str:
    return value


def deserialize_json(data: str) -> CodegenJobGenericDataSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CodegenJobGenericDataSourceType value: {data!r}"
        )
    return cast(CodegenJobGenericDataSourceType, data)
