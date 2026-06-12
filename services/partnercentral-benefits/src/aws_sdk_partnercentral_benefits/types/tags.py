"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.tag

Tags: TypeAlias = list["aws_sdk_partnercentral_benefits.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tags) -> list:
    import aws_sdk_partnercentral_benefits.types.tag

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.tag.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Tags:
    import aws_sdk_partnercentral_benefits.types.tag

    out: Tags = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.tag.deserialize_aws_json_1_0(item)
        )
    return out
