"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consistent_read
    import aws_sdk_dynamodb.types.parti_ql_statement
    import aws_sdk_dynamodb.types.prepared_statement_parameters
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure


class BatchStatementRequest(TypedDict):
    statement: "aws_sdk_dynamodb.types.parti_ql_statement.PartiQLStatement"
    """<p> A valid PartiQL statement. </p>"""
    parameters: NotRequired[
        "aws_sdk_dynamodb.types.prepared_statement_parameters.PreparedStatementParameters"
    ]
    """<p> The parameters associated with a PartiQL statement in the batch request. </p>"""
    consistent_read: NotRequired[
        "aws_sdk_dynamodb.types.consistent_read.ConsistentRead"
    ]
    """<p> The read consistency of the PartiQL batch request. </p>"""
    return_values_on_condition_check_failure: NotRequired[
        "aws_sdk_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for a PartiQL batch request operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchStatementRequest) -> dict:
    out: dict = {}
    out["Statement"] = value["statement"]
    if "parameters" in value:
        import aws_sdk_dynamodb.types.prepared_statement_parameters

        out["Parameters"] = (
            aws_sdk_dynamodb.types.prepared_statement_parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "consistent_read" in value:
        out["ConsistentRead"] = value["consistent_read"]
    if "return_values_on_condition_check_failure" in value:
        import aws_sdk_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            aws_sdk_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchStatementRequest:
    out: BatchStatementRequest = {}  # type: ignore[typeddict-item]
    if "Statement" in data:
        out["statement"] = data["Statement"]
    else:
        raise DeserializationError("BatchStatementRequest.statement required")
    if "Parameters" in data:
        import aws_sdk_dynamodb.types.prepared_statement_parameters

        out["parameters"] = (
            aws_sdk_dynamodb.types.prepared_statement_parameters.deserialize_aws_json_1_0(
                data["Parameters"]
            )
        )
    if "ConsistentRead" in data:
        out["consistent_read"] = data["ConsistentRead"]
    if "ReturnValuesOnConditionCheckFailure" in data:
        import aws_sdk_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            aws_sdk_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
