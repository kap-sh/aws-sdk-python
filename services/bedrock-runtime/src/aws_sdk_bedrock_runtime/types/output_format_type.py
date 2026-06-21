"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputFormatType``."""

from typing import Literal, TypeAlias, cast

"""<p> The type of structured output format. Available options are: json_schema. </p>"""
OutputFormatType: TypeAlias = Literal["json_schema",]


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormatType) -> str:
    return value


def deserialize_json(data: str) -> OutputFormatType:
    return cast(OutputFormatType, data)
