"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EngagementSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.ssm_contacts_arn

EngagementSet: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.ssm_contacts_arn.SsmContactsArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: EngagementSet) -> list:
    return list(value)


def deserialize_json(data: list) -> EngagementSet:
    return list(data)
