"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateRelationalDatabaseParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_parameter_list
    import aws_sdk_lightsail.types.resource_name


class UpdateRelationalDatabaseParametersRequest(TypedDict, closed=True):
    relational_database_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database for which to update parameters.</p>"""
    parameters: "aws_sdk_lightsail.types.relational_database_parameter_list.RelationalDatabaseParameterList"
    """<p>The database parameters to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRelationalDatabaseParametersRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    import aws_sdk_lightsail.types.relational_database_parameter_list

    out["parameters"] = (
        aws_sdk_lightsail.types.relational_database_parameter_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRelationalDatabaseParametersRequest:
    out: UpdateRelationalDatabaseParametersRequest = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseName" in data:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        raise DeserializationError(
            "UpdateRelationalDatabaseParametersRequest.relational_database_name required"
        )
    if "parameters" in data:
        import aws_sdk_lightsail.types.relational_database_parameter_list

        out["parameters"] = (
            aws_sdk_lightsail.types.relational_database_parameter_list.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRelationalDatabaseParametersRequest.parameters required"
        )
    return out
