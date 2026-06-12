"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_summary

DatastoreSummaries: TypeAlias = list[
    "aws_sdk_medical_imaging.types.datastore_summary.DatastoreSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreSummaries) -> list:
    import aws_sdk_medical_imaging.types.datastore_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_medical_imaging.types.datastore_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatastoreSummaries:
    import aws_sdk_medical_imaging.types.datastore_summary

    out: DatastoreSummaries = []
    for item in data:
        out.append(
            aws_sdk_medical_imaging.types.datastore_summary.deserialize_json(item)
        )
    return out
