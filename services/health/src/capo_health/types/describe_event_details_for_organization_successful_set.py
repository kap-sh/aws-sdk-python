"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsForOrganizationSuccessfulSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_event_details

DescribeEventDetailsForOrganizationSuccessfulSet: TypeAlias = list[
    "capo_health.types.organization_event_details.OrganizationEventDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeEventDetailsForOrganizationSuccessfulSet,
) -> list:
    import capo_health.types.organization_event_details

    out: list = []
    for item in value:
        out.append(
            capo_health.types.organization_event_details.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> DescribeEventDetailsForOrganizationSuccessfulSet:
    import capo_health.types.organization_event_details

    out: DescribeEventDetailsForOrganizationSuccessfulSet = []
    for item in data:
        out.append(
            capo_health.types.organization_event_details.deserialize_aws_json_1_1(item)
        )
    return out
