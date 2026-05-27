"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteTransactionInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.client_request_token
    import aws_sdk_dynamodb.types.parameterized_statements
    import aws_sdk_dynamodb.types.return_consumed_capacity


class ExecuteTransactionInput(TypedDict):
    transact_statements: (
        "aws_sdk_dynamodb.types.parameterized_statements.ParameterizedStatements"
    )
    """<p>The list of PartiQL statements representing the transaction to run.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_dynamodb.types.client_request_token.ClientRequestToken"
    ]
    """<p>Set this value to get remaining results, if <code>NextToken</code> was returned in the statement response.</p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    """<p>Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html\">TransactGetItems</a> and <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html\">TransactWriteItems</a>.</p>"""
