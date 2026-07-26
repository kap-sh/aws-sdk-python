"""Generated from Smithy shape ``com.amazonaws.cloudtrail#TagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.tag

TagsList: TypeAlias = list["capo_cloudtrail.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsList) -> list:
    import capo_cloudtrail.types.tag

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagsList:
    import capo_cloudtrail.types.tag

    out: TagsList = []
    for item in data:
        out.append(capo_cloudtrail.types.tag.deserialize_aws_json_1_1(item))
    return out
