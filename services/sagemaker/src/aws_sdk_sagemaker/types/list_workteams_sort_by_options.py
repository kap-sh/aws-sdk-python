"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListWorkteamsSortByOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListWorkteamsSortByOptions: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ListWorkteamsSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListWorkteamsSortByOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListWorkteamsSortByOptions value: {data!r}"
        )
    return cast(ListWorkteamsSortByOptions, data)
