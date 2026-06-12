"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSpeculativeDecodingTechnique``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelSpeculativeDecodingTechnique: TypeAlias = Literal["EAGLE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EAGLE",))


def serialize_aws_json_1_1(value: ModelSpeculativeDecodingTechnique) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSpeculativeDecodingTechnique:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ModelSpeculativeDecodingTechnique value: {data!r}"
        )
    return cast(ModelSpeculativeDecodingTechnique, data)
