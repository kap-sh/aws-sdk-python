"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_identifiers


class BatchDeleteEvaluationJobRequest(TypedDict):
    job_identifiers: (
        "aws_sdk_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers"
    )
    """<p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.evaluation_job_identifiers

    out["jobIdentifiers"] = (
        aws_sdk_bedrock.types.evaluation_job_identifiers.serialize_json(
            value["job_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobRequest:
    out: BatchDeleteEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    if "jobIdentifiers" in data:
        import aws_sdk_bedrock.types.evaluation_job_identifiers

        out["job_identifiers"] = (
            aws_sdk_bedrock.types.evaluation_job_identifiers.deserialize_json(
                data["jobIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteEvaluationJobRequest.job_identifiers required"
        )
    return out
