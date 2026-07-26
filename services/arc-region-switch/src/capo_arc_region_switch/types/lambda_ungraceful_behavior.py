"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

LambdaUngracefulBehavior: TypeAlias = Literal["skip",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaUngracefulBehavior:
    return cast(LambdaUngracefulBehavior, data)
