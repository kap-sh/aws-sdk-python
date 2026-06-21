"""Generated from Smithy shape ``com.amazonaws.route53resolver#BlockOverrideDnsType``."""

from typing import Literal, TypeAlias, cast

BlockOverrideDnsType: TypeAlias = Literal["CNAME",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockOverrideDnsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockOverrideDnsType:
    return cast(BlockOverrideDnsType, data)
