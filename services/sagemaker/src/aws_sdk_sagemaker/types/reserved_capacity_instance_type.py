"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacityInstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ReservedCapacityInstanceType: TypeAlias = Literal[
    "ml.p4d.24xlarge",
    "ml.p5.48xlarge",
    "ml.p5e.48xlarge",
    "ml.p5en.48xlarge",
    "ml.trn1.32xlarge",
    "ml.trn2.48xlarge",
    "ml.p6-b200.48xlarge",
    "ml.p4de.24xlarge",
    "ml.p6e-gb200.36xlarge",
    "ml.p5.4xlarge",
    "ml.p6-b300.48xlarge",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ml.p4d.24xlarge",
        "ml.p5.48xlarge",
        "ml.p5e.48xlarge",
        "ml.p5en.48xlarge",
        "ml.trn1.32xlarge",
        "ml.trn2.48xlarge",
        "ml.p6-b200.48xlarge",
        "ml.p4de.24xlarge",
        "ml.p6e-gb200.36xlarge",
        "ml.p5.4xlarge",
        "ml.p6-b300.48xlarge",
    )
)


def serialize_aws_json_1_1(value: ReservedCapacityInstanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReservedCapacityInstanceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReservedCapacityInstanceType value: {data!r}"
        )
    return cast(ReservedCapacityInstanceType, data)
