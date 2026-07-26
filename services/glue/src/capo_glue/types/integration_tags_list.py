"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.tag

IntegrationTagsList: TypeAlias = list["capo_glue.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationTagsList) -> list:
    import capo_glue.types.tag

    out: list = []
    for item in value:
        out.append(capo_glue.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationTagsList:
    import capo_glue.types.tag

    out: IntegrationTagsList = []
    for item in data:
        out.append(capo_glue.types.tag.deserialize_aws_json_1_1(item))
    return out
