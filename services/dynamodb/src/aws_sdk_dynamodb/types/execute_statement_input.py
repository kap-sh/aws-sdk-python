"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteStatementInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consistent_read
    import aws_sdk_dynamodb.types.parti_ql_next_token
    import aws_sdk_dynamodb.types.parti_ql_statement
    import aws_sdk_dynamodb.types.positive_integer_object
    import aws_sdk_dynamodb.types.prepared_statement_parameters
    import aws_sdk_dynamodb.types.return_consumed_capacity
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure


class ExecuteStatementInput(TypedDict):
    statement: "aws_sdk_dynamodb.types.parti_ql_statement.PartiQLStatement"
    """<p>The PartiQL statement representing the operation to run.</p>"""
    parameters: NotRequired[
        "aws_sdk_dynamodb.types.prepared_statement_parameters.PreparedStatementParameters"
    ]
    """<p>The parameters for the PartiQL statement, if any.</p>"""
    consistent_read: NotRequired[
        "aws_sdk_dynamodb.types.consistent_read.ConsistentRead"
    ]
    """<p>The consistency of a read operation. If set to <code>true</code>, then a strongly consistent read is used; otherwise, an eventually consistent read is used.</p>"""
    next_token: NotRequired[
        "aws_sdk_dynamodb.types.parti_ql_next_token.PartiQLNextToken"
    ]
    """<p>Set this value to get remaining results, if <code>NextToken</code> was returned in the statement response.</p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    limit: NotRequired[
        "aws_sdk_dynamodb.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, along with a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation so you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. </p>"""
    return_values_on_condition_check_failure: NotRequired[
        "aws_sdk_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for an <code>ExecuteStatement</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""
