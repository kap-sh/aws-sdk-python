"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.tag

Tags: TypeAlias = list["capo_partnercentral_benefits.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tags) -> list:
    import capo_partnercentral_benefits.types.tag

    out: list = []
    for item in value:
        out.append(capo_partnercentral_benefits.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Tags:
    import capo_partnercentral_benefits.types.tag

    out: Tags = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.tag.deserialize_aws_json_1_0(item)
        )
    return out
