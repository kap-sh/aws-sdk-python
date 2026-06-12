"""Generated from Smithy shape ``com.amazonaws.snowball#LambdaResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.lambda_resource

LambdaResourceList: TypeAlias = list[
    "aws_sdk_snowball.types.lambda_resource.LambdaResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaResourceList) -> list:
    import aws_sdk_snowball.types.lambda_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_snowball.types.lambda_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LambdaResourceList:
    import aws_sdk_snowball.types.lambda_resource

    out: LambdaResourceList = []
    for item in data:
        out.append(
            aws_sdk_snowball.types.lambda_resource.deserialize_aws_json_1_1(item)
        )
    return out
