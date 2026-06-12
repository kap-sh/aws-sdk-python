"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_identifier

EvaluationJobIdentifiers: TypeAlias = list[
    "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationJobIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationJobIdentifiers:
    return list(data)
