"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActiveClusterOperationName``."""

from typing import Literal, TypeAlias, cast

ActiveClusterOperationName: TypeAlias = Literal["Scaling",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveClusterOperationName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActiveClusterOperationName:
    return cast(ActiveClusterOperationName, data)
