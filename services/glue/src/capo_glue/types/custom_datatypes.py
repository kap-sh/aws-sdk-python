"""Generated from Smithy shape ``com.amazonaws.glue#CustomDatatypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

CustomDatatypes: TypeAlias = list["capo_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomDatatypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomDatatypes:
    return list(data)
