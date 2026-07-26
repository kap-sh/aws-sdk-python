"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.resource_identifier

ResourceIdentifierList: TypeAlias = list[
    "capo_config_service.types.resource_identifier.ResourceIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceIdentifierList) -> list:
    import capo_config_service.types.resource_identifier

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.resource_identifier.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceIdentifierList:
    import capo_config_service.types.resource_identifier

    out: ResourceIdentifierList = []
    for item in data:
        out.append(
            capo_config_service.types.resource_identifier.deserialize_aws_json_1_1(item)
        )
    return out
