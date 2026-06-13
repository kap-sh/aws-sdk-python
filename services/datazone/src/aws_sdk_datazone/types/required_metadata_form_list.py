"""Generated from Smithy shape ``com.amazonaws.datazone#RequiredMetadataFormList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_form_reference

RequiredMetadataFormList: TypeAlias = list[
    "aws_sdk_datazone.types.metadata_form_reference.MetadataFormReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredMetadataFormList) -> list:
    import aws_sdk_datazone.types.metadata_form_reference

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.metadata_form_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequiredMetadataFormList:
    import aws_sdk_datazone.types.metadata_form_reference

    out: RequiredMetadataFormList = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.metadata_form_reference.deserialize_json(item)
        )
    return out
