"""Generated from Smithy shape ``com.amazonaws.deadline#ManifestPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.manifest_properties

ManifestPropertiesList: TypeAlias = list[
    "aws_sdk_deadline.types.manifest_properties.ManifestProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManifestPropertiesList) -> list:
    import aws_sdk_deadline.types.manifest_properties

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.manifest_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> ManifestPropertiesList:
    import aws_sdk_deadline.types.manifest_properties

    out: ManifestPropertiesList = []
    for item in data:
        out.append(aws_sdk_deadline.types.manifest_properties.deserialize_json(item))
    return out
