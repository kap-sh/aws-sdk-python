"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSdiSourceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.sdi_source_summary

__listOfSdiSourceSummary: TypeAlias = list[
    "capo_medialive.types.sdi_source_summary.SdiSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSdiSourceSummary) -> list:
    import capo_medialive.types.sdi_source_summary

    out: list = []
    for item in value:
        out.append(capo_medialive.types.sdi_source_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSdiSourceSummary:
    import capo_medialive.types.sdi_source_summary

    out: __listOfSdiSourceSummary = []
    for item in data:
        out.append(capo_medialive.types.sdi_source_summary.deserialize_json(item))
    return out
