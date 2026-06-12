"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Matches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.match

Matches: TypeAlias = list["aws_sdk_codeguruprofiler.types.match.Match"]


# --- restJson1 ser/de ---
def serialize_json(value: Matches) -> list:
    import aws_sdk_codeguruprofiler.types.match

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguruprofiler.types.match.serialize_json(item))
    return out


def deserialize_json(data: list) -> Matches:
    import aws_sdk_codeguruprofiler.types.match

    out: Matches = []
    for item in data:
        out.append(aws_sdk_codeguruprofiler.types.match.deserialize_json(item))
    return out
