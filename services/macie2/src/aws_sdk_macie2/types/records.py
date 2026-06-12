"""Generated from Smithy shape ``com.amazonaws.macie2#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.record

Records: TypeAlias = list["aws_sdk_macie2.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: Records) -> list:
    import aws_sdk_macie2.types.record

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> Records:
    import aws_sdk_macie2.types.record

    out: Records = []
    for item in data:
        out.append(aws_sdk_macie2.types.record.deserialize_json(item))
    return out
