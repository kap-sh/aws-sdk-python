"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.batch_job_definitions
    import aws_sdk_m2.types.next_token


class ListBatchJobDefinitionsResponse(TypedDict):
    batch_job_definitions: "aws_sdk_m2.types.batch_job_definitions.BatchJobDefinitions"
    """<p>The list of batch job definitions.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobDefinitionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.batch_job_definitions

    out["batchJobDefinitions"] = aws_sdk_m2.types.batch_job_definitions.serialize_json(
        value["batch_job_definitions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBatchJobDefinitionsResponse:
    out: ListBatchJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "batchJobDefinitions" in data:
        import aws_sdk_m2.types.batch_job_definitions

        out["batch_job_definitions"] = (
            aws_sdk_m2.types.batch_job_definitions.deserialize_json(
                data["batchJobDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "ListBatchJobDefinitionsResponse.batch_job_definitions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
