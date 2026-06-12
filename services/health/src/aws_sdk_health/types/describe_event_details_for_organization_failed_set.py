"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsForOrganizationFailedSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.organization_event_details_error_item

DescribeEventDetailsForOrganizationFailedSet: TypeAlias = list[
    "aws_sdk_health.types.organization_event_details_error_item.OrganizationEventDetailsErrorItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventDetailsForOrganizationFailedSet) -> list:
    import aws_sdk_health.types.organization_event_details_error_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_health.types.organization_event_details_error_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> DescribeEventDetailsForOrganizationFailedSet:
    import aws_sdk_health.types.organization_event_details_error_item

    out: DescribeEventDetailsForOrganizationFailedSet = []
    for item in data:
        out.append(
            aws_sdk_health.types.organization_event_details_error_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
