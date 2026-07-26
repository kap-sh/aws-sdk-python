"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_summary

DatastoreSummaries: TypeAlias = list[
    "capo_medical_imaging.types.datastore_summary.DatastoreSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreSummaries) -> list:
    import capo_medical_imaging.types.datastore_summary

    out: list = []
    for item in value:
        out.append(capo_medical_imaging.types.datastore_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatastoreSummaries:
    import capo_medical_imaging.types.datastore_summary

    out: DatastoreSummaries = []
    for item in data:
        out.append(capo_medical_imaging.types.datastore_summary.deserialize_json(item))
    return out
