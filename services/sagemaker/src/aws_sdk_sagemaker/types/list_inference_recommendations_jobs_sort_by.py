"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListInferenceRecommendationsJobsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListInferenceRecommendationsJobsSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListInferenceRecommendationsJobsSortBy value: {data!r}"
        )
    return cast(ListInferenceRecommendationsJobsSortBy, data)
