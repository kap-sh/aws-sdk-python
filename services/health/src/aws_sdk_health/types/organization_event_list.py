"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.organization_event

OrganizationEventList: TypeAlias = list[
    "aws_sdk_health.types.organization_event.OrganizationEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventList) -> list:
    import aws_sdk_health.types.organization_event

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.organization_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEventList:
    import aws_sdk_health.types.organization_event

    out: OrganizationEventList = []
    for item in data:
        out.append(
            aws_sdk_health.types.organization_event.deserialize_aws_json_1_1(item)
        )
    return out
