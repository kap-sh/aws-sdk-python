"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityAggregatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.organization_entity_aggregate

OrganizationEntityAggregatesList: TypeAlias = list[
    "aws_sdk_health.types.organization_entity_aggregate.OrganizationEntityAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityAggregatesList) -> list:
    import aws_sdk_health.types.organization_entity_aggregate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_health.types.organization_entity_aggregate.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEntityAggregatesList:
    import aws_sdk_health.types.organization_entity_aggregate

    out: OrganizationEntityAggregatesList = []
    for item in data:
        out.append(
            aws_sdk_health.types.organization_entity_aggregate.deserialize_aws_json_1_1(
                item
            )
        )
    return out
