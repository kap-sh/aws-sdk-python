"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActiveClusterOperationName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ActiveClusterOperationName: TypeAlias = Literal["Scaling",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Scaling",))


def serialize_aws_json_1_1(value: ActiveClusterOperationName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActiveClusterOperationName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ActiveClusterOperationName value: {data!r}"
        )
    return cast(ActiveClusterOperationName, data)
