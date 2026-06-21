"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobGenericDataSourceType``."""

from typing import Literal, TypeAlias, cast

CodegenJobGenericDataSourceType: TypeAlias = Literal["DataStore",]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobGenericDataSourceType) -> str:
    return value


def deserialize_json(data: str) -> CodegenJobGenericDataSourceType:
    return cast(CodegenJobGenericDataSourceType, data)
