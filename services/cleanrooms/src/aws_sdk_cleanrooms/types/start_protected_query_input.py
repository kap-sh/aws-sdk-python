"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartProtectedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.compute_configuration
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_query_result_configuration
    import aws_sdk_cleanrooms.types.protected_query_sql_parameters
    import aws_sdk_cleanrooms.types.protected_query_type


class StartProtectedQueryInput(TypedDict, closed=True):
    type: "aws_sdk_cleanrooms.types.protected_query_type.ProtectedQueryType"
    """<p>The type of the protected query to be started.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership to run this query against. Currently accepts a membership ID.</p>"""
    sql_parameters: "aws_sdk_cleanrooms.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    """<p>The protected SQL query parameters.</p>"""
    result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.protected_query_result_configuration.ProtectedQueryResultConfiguration"
    ]
    """<p>The details needed to write the query results.</p>"""
    compute_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.compute_configuration.ComputeConfiguration"
    ]
    """<p> The compute configuration for the protected query.</p>"""
    query_compute_payer_account_id: NotRequired[
        "aws_sdk_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the query compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProtectedQueryInput) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import aws_sdk_cleanrooms.types.protected_query_sql_parameters

    out["sqlParameters"] = (
        aws_sdk_cleanrooms.types.protected_query_sql_parameters.serialize_json(
            value["sql_parameters"]
        )
    )
    if "result_configuration" in value:
        import aws_sdk_cleanrooms.types.protected_query_result_configuration

        out["resultConfiguration"] = (
            aws_sdk_cleanrooms.types.protected_query_result_configuration.serialize_json(
                value["result_configuration"]
            )
        )
    if "compute_configuration" in value:
        import aws_sdk_cleanrooms.types.compute_configuration

        out["computeConfiguration"] = (
            aws_sdk_cleanrooms.types.compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    if "query_compute_payer_account_id" in value:
        out["queryComputePayerAccountId"] = value["query_compute_payer_account_id"]
    return out


def deserialize_json(data: dict) -> StartProtectedQueryInput:
    out: StartProtectedQueryInput = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("StartProtectedQueryInput.type required")
    if "sqlParameters" in data:
        import aws_sdk_cleanrooms.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            aws_sdk_cleanrooms.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    else:
        raise DeserializationError("StartProtectedQueryInput.sql_parameters required")
    if "resultConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_query_result_configuration

        out["result_configuration"] = (
            aws_sdk_cleanrooms.types.protected_query_result_configuration.deserialize_json(
                data["resultConfiguration"]
            )
        )
    if "computeConfiguration" in data:
        import aws_sdk_cleanrooms.types.compute_configuration

        out["compute_configuration"] = (
            aws_sdk_cleanrooms.types.compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if "queryComputePayerAccountId" in data:
        out["query_compute_payer_account_id"] = data["queryComputePayerAccountId"]
    return out
