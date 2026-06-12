"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfTag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.tag

ListOfTag: TypeAlias = list["aws_sdk_dataexchange.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTag) -> list:
    import aws_sdk_dataexchange.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_dataexchange.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTag:
    import aws_sdk_dataexchange.types.tag

    out: ListOfTag = []
    for item in data:
        out.append(aws_sdk_dataexchange.types.tag.deserialize_json(item))
    return out
