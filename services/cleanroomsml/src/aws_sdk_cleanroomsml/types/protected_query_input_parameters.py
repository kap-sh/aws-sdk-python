"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ProtectedQueryInputParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.compute_configuration
    import aws_sdk_cleanroomsml.types.protected_query_sql_parameters
    import aws_sdk_cleanroomsml.types.result_format


class ProtectedQueryInputParameters(TypedDict, closed=True):
    sql_parameters: "aws_sdk_cleanroomsml.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    compute_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.compute_configuration.ComputeConfiguration"
    ]
    """<p>Provides configuration information for the workers that will perform the protected query.</p>"""
    result_format: "aws_sdk_cleanroomsml.types.result_format.ResultFormat"
    """<p>The format in which the query results should be returned. If not specified, defaults to <code>CSV</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryInputParameters) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.protected_query_sql_parameters

    out["sqlParameters"] = (
        aws_sdk_cleanroomsml.types.protected_query_sql_parameters.serialize_json(
            value["sql_parameters"]
        )
    )
    if "compute_configuration" in value:
        import aws_sdk_cleanroomsml.types.compute_configuration

        out["computeConfiguration"] = (
            aws_sdk_cleanroomsml.types.compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    import aws_sdk_cleanroomsml.types.result_format

    out["resultFormat"] = aws_sdk_cleanroomsml.types.result_format.serialize_json(
        value.get("result_format", "CSV")
    )
    return out


def deserialize_json(data: dict) -> ProtectedQueryInputParameters:
    out: ProtectedQueryInputParameters = {}  # type: ignore[typeddict-item]
    if "sqlParameters" in data:
        import aws_sdk_cleanroomsml.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            aws_sdk_cleanroomsml.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedQueryInputParameters.sql_parameters required"
        )
    if "computeConfiguration" in data:
        import aws_sdk_cleanroomsml.types.compute_configuration

        out["compute_configuration"] = (
            aws_sdk_cleanroomsml.types.compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if "resultFormat" in data:
        import aws_sdk_cleanroomsml.types.result_format

        out["result_format"] = (
            aws_sdk_cleanroomsml.types.result_format.deserialize_json(
                data["resultFormat"]
            )
        )
    else:
        out["result_format"] = "CSV"
    return out
