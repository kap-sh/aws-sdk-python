"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
