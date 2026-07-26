"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEntityFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_account_filter

OrganizationEntityFiltersList: TypeAlias = list[
    "capo_health.types.event_account_filter.EventAccountFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEntityFiltersList) -> list:
    import capo_health.types.event_account_filter

    out: list = []
    for item in value:
        out.append(capo_health.types.event_account_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEntityFiltersList:
    import capo_health.types.event_account_filter

    out: OrganizationEntityFiltersList = []
    for item in data:
        out.append(
            capo_health.types.event_account_filter.deserialize_aws_json_1_1(item)
        )
    return out
