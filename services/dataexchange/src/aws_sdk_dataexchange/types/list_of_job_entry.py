"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfJobEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.job_entry

ListOfJobEntry: TypeAlias = list["aws_sdk_dataexchange.types.job_entry.JobEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJobEntry) -> list:
    import aws_sdk_dataexchange.types.job_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_dataexchange.types.job_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJobEntry:
    import aws_sdk_dataexchange.types.job_entry

    out: ListOfJobEntry = []
    for item in data:
        out.append(aws_sdk_dataexchange.types.job_entry.deserialize_json(item))
    return out
