"""Generated from Smithy shape ``com.amazonaws.dynamodb#PartiQLBatchRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.batch_statement_request

PartiQLBatchRequest: TypeAlias = list[
    "capo_dynamodb.types.batch_statement_request.BatchStatementRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartiQLBatchRequest) -> list:
    import capo_dynamodb.types.batch_statement_request

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.batch_statement_request.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartiQLBatchRequest:
    import capo_dynamodb.types.batch_statement_request

    out: PartiQLBatchRequest = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.batch_statement_request.deserialize_aws_json_1_0(item)
        )
    return out
