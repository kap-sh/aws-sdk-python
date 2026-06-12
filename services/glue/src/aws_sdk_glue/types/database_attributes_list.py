"""Generated from Smithy shape ``com.amazonaws.glue#DatabaseAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.database_attributes

DatabaseAttributesList: TypeAlias = list[
    "aws_sdk_glue.types.database_attributes.DatabaseAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseAttributesList) -> list:
    import aws_sdk_glue.types.database_attributes

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.database_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DatabaseAttributesList:
    import aws_sdk_glue.types.database_attributes

    out: DatabaseAttributesList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.database_attributes.deserialize_aws_json_1_1(item)
        )
    return out
