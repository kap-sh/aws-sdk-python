"""Generated from Smithy shape ``com.amazonaws.dynamodb#ParameterizedStatement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.parti_ql_statement
    import aws_sdk_dynamodb.types.prepared_statement_parameters
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure


class ParameterizedStatement(TypedDict):
    statement: "aws_sdk_dynamodb.types.parti_ql_statement.PartiQLStatement"
    """<p> A PartiQL statement that uses parameters. </p>"""
    parameters: NotRequired[
        "aws_sdk_dynamodb.types.prepared_statement_parameters.PreparedStatementParameters"
    ]
    """<p> The parameter values. </p>"""
    return_values_on_condition_check_failure: NotRequired[
        "aws_sdk_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for a PartiQL <code>ParameterizedStatement</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""
