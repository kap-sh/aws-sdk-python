"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

"""<p> The type of structured output format. Available options are: json_schema. </p>"""
OutputFormatType: TypeAlias = Literal["json_schema",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("json_schema",))


def serialize_json(value: OutputFormatType) -> str:
    return value


def deserialize_json(data: str) -> OutputFormatType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormatType value: {data!r}")
    return cast(OutputFormatType, data)
