"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormsSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_form_summary

MetadataFormsSummary: TypeAlias = list[
    "aws_sdk_datazone.types.metadata_form_summary.MetadataFormSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormsSummary) -> list:
    import aws_sdk_datazone.types.metadata_form_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.metadata_form_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataFormsSummary:
    import aws_sdk_datazone.types.metadata_form_summary

    out: MetadataFormsSummary = []
    for item in data:
        out.append(aws_sdk_datazone.types.metadata_form_summary.deserialize_json(item))
    return out
