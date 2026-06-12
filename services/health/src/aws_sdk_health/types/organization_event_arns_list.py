"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_arn

OrganizationEventArnsList: TypeAlias = list["aws_sdk_health.types.event_arn.eventArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventArnsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationEventArnsList:
    return list(data)
