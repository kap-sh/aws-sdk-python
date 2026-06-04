"""Generated from Smithy shape ``com.amazonaws.dynamodb#PartiQLBatchResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.batch_statement_response

PartiQLBatchResponse: TypeAlias = list[
    "aws_sdk_dynamodb.types.batch_statement_response.BatchStatementResponse"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartiQLBatchResponse) -> list:
    import aws_sdk_dynamodb.types.batch_statement_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.batch_statement_response.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartiQLBatchResponse:
    import aws_sdk_dynamodb.types.batch_statement_response

    out: PartiQLBatchResponse = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.batch_statement_response.deserialize_aws_json_1_0(
                item
            )
        )
    return out
