"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceIdentifiersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_resource_identifier

ResourceIdentifiersList: TypeAlias = list[
    "aws_sdk_config_service.types.aggregate_resource_identifier.AggregateResourceIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceIdentifiersList) -> list:
    import aws_sdk_config_service.types.aggregate_resource_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.aggregate_resource_identifier.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceIdentifiersList:
    import aws_sdk_config_service.types.aggregate_resource_identifier

    out: ResourceIdentifiersList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.aggregate_resource_identifier.deserialize_aws_json_1_1(
                item
            )
        )
    return out
