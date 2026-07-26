"""Generated from Smithy shape ``com.amazonaws.inspector#AssetType``."""

from typing import Literal, TypeAlias, cast

AssetType: TypeAlias = Literal["ec2-instance",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssetType:
    return cast(AssetType, data)
