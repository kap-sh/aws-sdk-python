"""Generated from Smithy shape ``com.amazonaws.dynamodb#ParameterizedStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterizedStatement) -> dict:
    out: dict = {}
    out["Statement"] = value["statement"]
    if "parameters" in value:
        import aws_sdk_dynamodb.types.prepared_statement_parameters

        out["Parameters"] = (
            aws_sdk_dynamodb.types.prepared_statement_parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "return_values_on_condition_check_failure" in value:
        import aws_sdk_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            aws_sdk_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ParameterizedStatement:
    out: ParameterizedStatement = {}  # type: ignore[typeddict-item]
    if "Statement" in data:
        out["statement"] = data["Statement"]
    else:
        raise DeserializationError("ParameterizedStatement.statement required")
    if "Parameters" in data:
        import aws_sdk_dynamodb.types.prepared_statement_parameters

        out["parameters"] = (
            aws_sdk_dynamodb.types.prepared_statement_parameters.deserialize_aws_json_1_0(
                data["Parameters"]
            )
        )
    if "ReturnValuesOnConditionCheckFailure" in data:
        import aws_sdk_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            aws_sdk_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
