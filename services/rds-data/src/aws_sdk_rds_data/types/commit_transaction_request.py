"""Generated from Smithy shape ``com.amazonaws.rdsdata#CommitTransactionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.arn
    import aws_sdk_rds_data.types.id


class CommitTransactionRequest(TypedDict):
    resource_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The name or ARN of the secret that enables access to the DB cluster.</p>"""
    transaction_id: "aws_sdk_rds_data.types.id.Id"
    """<p>The identifier of the transaction to end and commit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommitTransactionRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["transactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> CommitTransactionRequest:
    out: CommitTransactionRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("CommitTransactionRequest.resource_arn required")
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("CommitTransactionRequest.secret_arn required")
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    else:
        raise DeserializationError("CommitTransactionRequest.transaction_id required")
    return out
