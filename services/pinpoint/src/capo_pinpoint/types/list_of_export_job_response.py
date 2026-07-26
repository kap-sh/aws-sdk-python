"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfExportJobResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.export_job_response

ListOfExportJobResponse: TypeAlias = list[
    "capo_pinpoint.types.export_job_response.ExportJobResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfExportJobResponse) -> list:
    import capo_pinpoint.types.export_job_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.export_job_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfExportJobResponse:
    import capo_pinpoint.types.export_job_response

    out: ListOfExportJobResponse = []
    for item in data:
        out.append(capo_pinpoint.types.export_job_response.deserialize_json(item))
    return out
