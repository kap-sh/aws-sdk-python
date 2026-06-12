"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_translate.types.terminology_properties

TerminologyPropertiesList: TypeAlias = list[
    "aws_sdk_translate.types.terminology_properties.TerminologyProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyPropertiesList) -> list:
    import aws_sdk_translate.types.terminology_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_translate.types.terminology_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TerminologyPropertiesList:
    import aws_sdk_translate.types.terminology_properties

    out: TerminologyPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_translate.types.terminology_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
