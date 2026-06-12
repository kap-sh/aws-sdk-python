"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfSensitivityInspectionTemplatesEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.sensitivity_inspection_templates_entry

__listOfSensitivityInspectionTemplatesEntry: TypeAlias = list[
    "aws_sdk_macie2.types.sensitivity_inspection_templates_entry.SensitivityInspectionTemplatesEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSensitivityInspectionTemplatesEntry) -> list:
    import aws_sdk_macie2.types.sensitivity_inspection_templates_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_macie2.types.sensitivity_inspection_templates_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfSensitivityInspectionTemplatesEntry:
    import aws_sdk_macie2.types.sensitivity_inspection_templates_entry

    out: __listOfSensitivityInspectionTemplatesEntry = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.sensitivity_inspection_templates_entry.deserialize_json(
                item
            )
        )
    return out
