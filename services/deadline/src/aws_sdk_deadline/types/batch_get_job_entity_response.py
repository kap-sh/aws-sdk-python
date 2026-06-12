"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobEntityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_job_entity_errors
    import aws_sdk_deadline.types.batch_get_job_entity_list


class BatchGetJobEntityResponse(TypedDict):
    entities: "aws_sdk_deadline.types.batch_get_job_entity_list.BatchGetJobEntityList"
    """<p>A list of the job entities, or details, in the batch.</p>"""
    errors: "aws_sdk_deadline.types.batch_get_job_entity_errors.BatchGetJobEntityErrors"
    """<p>A list of errors from the job error logs for the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobEntityResponse) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.batch_get_job_entity_list

    out["entities"] = aws_sdk_deadline.types.batch_get_job_entity_list.serialize_json(
        value["entities"]
    )
    import aws_sdk_deadline.types.batch_get_job_entity_errors

    out["errors"] = aws_sdk_deadline.types.batch_get_job_entity_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobEntityResponse:
    out: BatchGetJobEntityResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_deadline.types.batch_get_job_entity_list

        out["entities"] = (
            aws_sdk_deadline.types.batch_get_job_entity_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("BatchGetJobEntityResponse.entities required")
    if "errors" in data:
        import aws_sdk_deadline.types.batch_get_job_entity_errors

        out["errors"] = (
            aws_sdk_deadline.types.batch_get_job_entity_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetJobEntityResponse.errors required")
    return out
