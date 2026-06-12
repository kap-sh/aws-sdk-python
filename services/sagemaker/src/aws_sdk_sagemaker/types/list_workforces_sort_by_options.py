"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListWorkforcesSortByOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListWorkforcesSortByOptions: TypeAlias = Literal[
    "Name",
    "CreateDate",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreateDate",
    )
)


def serialize_aws_json_1_1(value: ListWorkforcesSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListWorkforcesSortByOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListWorkforcesSortByOptions value: {data!r}"
        )
    return cast(ListWorkforcesSortByOptions, data)
