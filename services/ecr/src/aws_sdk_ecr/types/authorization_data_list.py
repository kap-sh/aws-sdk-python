"""Generated from Smithy shape ``com.amazonaws.ecr#AuthorizationDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.authorization_data

AuthorizationDataList: TypeAlias = list[
    "aws_sdk_ecr.types.authorization_data.AuthorizationData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizationDataList) -> list:
    import aws_sdk_ecr.types.authorization_data

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.authorization_data.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AuthorizationDataList:
    import aws_sdk_ecr.types.authorization_data

    out: AuthorizationDataList = []
    for item in data:
        out.append(aws_sdk_ecr.types.authorization_data.deserialize_aws_json_1_1(item))
    return out
