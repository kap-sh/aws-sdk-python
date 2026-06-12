"""Generated from Smithy shape ``com.amazonaws.kendra#EntityFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.alfresco_entity

EntityFilter: TypeAlias = list["aws_sdk_kendra.types.alfresco_entity.AlfrescoEntity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilter) -> list:
    import aws_sdk_kendra.types.alfresco_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.alfresco_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityFilter:
    import aws_sdk_kendra.types.alfresco_entity

    out: EntityFilter = []
    for item in data:
        out.append(aws_sdk_kendra.types.alfresco_entity.deserialize_aws_json_1_1(item))
    return out
