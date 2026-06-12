"""Generated from Smithy shape ``com.amazonaws.health#AccountEntityAggregatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.account_entity_aggregate

AccountEntityAggregatesList: TypeAlias = list[
    "aws_sdk_health.types.account_entity_aggregate.AccountEntityAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountEntityAggregatesList) -> list:
    import aws_sdk_health.types.account_entity_aggregate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_health.types.account_entity_aggregate.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountEntityAggregatesList:
    import aws_sdk_health.types.account_entity_aggregate

    out: AccountEntityAggregatesList = []
    for item in data:
        out.append(
            aws_sdk_health.types.account_entity_aggregate.deserialize_aws_json_1_1(item)
        )
    return out
