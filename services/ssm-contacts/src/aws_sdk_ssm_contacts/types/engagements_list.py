"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#EngagementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.engagement

EngagementsList: TypeAlias = list["aws_sdk_ssm_contacts.types.engagement.Engagement"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngagementsList) -> list:
    import aws_sdk_ssm_contacts.types.engagement

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.engagement.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EngagementsList:
    import aws_sdk_ssm_contacts.types.engagement

    out: EngagementsList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.engagement.deserialize_aws_json_1_1(item))
    return out
