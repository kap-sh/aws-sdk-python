"""Generated from Smithy shape ``com.amazonaws.ssm#RelatedOpsItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.related_ops_item

RelatedOpsItems: TypeAlias = list["aws_sdk_ssm.types.related_ops_item.RelatedOpsItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedOpsItems) -> list:
    import aws_sdk_ssm.types.related_ops_item

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.related_ops_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RelatedOpsItems:
    import aws_sdk_ssm.types.related_ops_item

    out: RelatedOpsItems = []
    for item in data:
        out.append(aws_sdk_ssm.types.related_ops_item.deserialize_aws_json_1_1(item))
    return out
