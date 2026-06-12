"""Generated from Smithy shape ``com.amazonaws.configservice#DiscoveredResourceIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_resource_identifier

DiscoveredResourceIdentifierList: TypeAlias = list[
    "aws_sdk_config_service.types.aggregate_resource_identifier.AggregateResourceIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResourceIdentifierList) -> list:
    import aws_sdk_config_service.types.aggregate_resource_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.aggregate_resource_identifier.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DiscoveredResourceIdentifierList:
    import aws_sdk_config_service.types.aggregate_resource_identifier

    out: DiscoveredResourceIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.aggregate_resource_identifier.deserialize_aws_json_1_1(
                item
            )
        )
    return out
