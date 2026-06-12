"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventDetailFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_account_filter

OrganizationEventDetailFiltersList: TypeAlias = list[
    "aws_sdk_health.types.event_account_filter.EventAccountFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventDetailFiltersList) -> list:
    import aws_sdk_health.types.event_account_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_health.types.event_account_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEventDetailFiltersList:
    import aws_sdk_health.types.event_account_filter

    out: OrganizationEventDetailFiltersList = []
    for item in data:
        out.append(
            aws_sdk_health.types.event_account_filter.deserialize_aws_json_1_1(item)
        )
    return out
