"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfImportJobResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.import_job_response

ListOfImportJobResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.import_job_response.ImportJobResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfImportJobResponse) -> list:
    import aws_sdk_pinpoint.types.import_job_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.import_job_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfImportJobResponse:
    import aws_sdk_pinpoint.types.import_job_response

    out: ListOfImportJobResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.import_job_response.deserialize_json(item))
    return out
