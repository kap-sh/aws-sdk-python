"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfRevisionEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.revision_entry

ListOfRevisionEntry: TypeAlias = list[
    "aws_sdk_dataexchange.types.revision_entry.RevisionEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRevisionEntry) -> list:
    import aws_sdk_dataexchange.types.revision_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_dataexchange.types.revision_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfRevisionEntry:
    import aws_sdk_dataexchange.types.revision_entry

    out: ListOfRevisionEntry = []
    for item in data:
        out.append(aws_sdk_dataexchange.types.revision_entry.deserialize_json(item))
    return out
