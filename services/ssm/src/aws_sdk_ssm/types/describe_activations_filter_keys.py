"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeActivationsFilterKeys``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DescribeActivationsFilterKeys: TypeAlias = Literal[
    "ActivationIds",
    "DefaultInstanceName",
    "IamRole",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ActivationIds",
        "DefaultInstanceName",
        "IamRole",
    )
)


def serialize_aws_json_1_1(value: DescribeActivationsFilterKeys) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeActivationsFilterKeys:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribeActivationsFilterKeys value: {data!r}"
        )
    return cast(DescribeActivationsFilterKeys, data)
