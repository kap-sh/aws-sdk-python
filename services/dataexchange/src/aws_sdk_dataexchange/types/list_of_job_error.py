"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfJobError``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.job_error

ListOfJobError: TypeAlias = list["aws_sdk_dataexchange.types.job_error.JobError"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJobError) -> list:
    import aws_sdk_dataexchange.types.job_error

    out: list = []
    for item in value:
        out.append(aws_sdk_dataexchange.types.job_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJobError:
    import aws_sdk_dataexchange.types.job_error

    out: ListOfJobError = []
    for item in data:
        out.append(aws_sdk_dataexchange.types.job_error.deserialize_json(item))
    return out
