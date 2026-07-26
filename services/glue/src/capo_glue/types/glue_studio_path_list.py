"""Generated from Smithy shape ``com.amazonaws.glue#GlueStudioPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_properties

GlueStudioPathList: TypeAlias = list[
    "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueStudioPathList) -> list:
    import capo_glue.types.enclosed_in_string_properties

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GlueStudioPathList:
    import capo_glue.types.enclosed_in_string_properties

    out: GlueStudioPathList = []
    for item in data:
        out.append(
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(item)
        )
    return out
