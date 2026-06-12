"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PublicKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.public_key

PublicKeyList: TypeAlias = list["aws_sdk_cloudtrail.types.public_key.PublicKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicKeyList) -> list:
    import aws_sdk_cloudtrail.types.public_key

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudtrail.types.public_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PublicKeyList:
    import aws_sdk_cloudtrail.types.public_key

    out: PublicKeyList = []
    for item in data:
        out.append(aws_sdk_cloudtrail.types.public_key.deserialize_aws_json_1_1(item))
    return out
