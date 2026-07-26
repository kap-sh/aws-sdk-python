"""Generated from Smithy shape ``com.amazonaws.health#AccountEntityAggregatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.account_entity_aggregate

AccountEntityAggregatesList: TypeAlias = list[
    "capo_health.types.account_entity_aggregate.AccountEntityAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountEntityAggregatesList) -> list:
    import capo_health.types.account_entity_aggregate

    out: list = []
    for item in value:
        out.append(
            capo_health.types.account_entity_aggregate.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountEntityAggregatesList:
    import capo_health.types.account_entity_aggregate

    out: AccountEntityAggregatesList = []
    for item in data:
        out.append(
            capo_health.types.account_entity_aggregate.deserialize_aws_json_1_1(item)
        )
    return out
