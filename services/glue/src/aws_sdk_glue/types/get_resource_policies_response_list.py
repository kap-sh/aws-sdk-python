"""Generated from Smithy shape ``com.amazonaws.glue#GetResourcePoliciesResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_policy

GetResourcePoliciesResponseList: TypeAlias = list[
    "aws_sdk_glue.types.glue_policy.GluePolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesResponseList) -> list:
    import aws_sdk_glue.types.glue_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.glue_policy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GetResourcePoliciesResponseList:
    import aws_sdk_glue.types.glue_policy

    out: GetResourcePoliciesResponseList = []
    for item in data:
        out.append(aws_sdk_glue.types.glue_policy.deserialize_aws_json_1_1(item))
    return out
