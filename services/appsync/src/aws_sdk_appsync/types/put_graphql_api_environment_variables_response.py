"""Generated from Smithy shape ``com.amazonaws.appsync#PutGraphqlApiEnvironmentVariablesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.environment_variable_map


class PutGraphqlApiEnvironmentVariablesResponse(TypedDict):
    environment_variables: NotRequired[
        "aws_sdk_appsync.types.environment_variable_map.EnvironmentVariableMap"
    ]
    """<p>The payload containing each environmental variable in the <code>\"key\" : \"value\"</code> format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGraphqlApiEnvironmentVariablesResponse) -> dict:
    out: dict = {}
    if "environment_variables" in value:
        import aws_sdk_appsync.types.environment_variable_map

        out["environmentVariables"] = (
            aws_sdk_appsync.types.environment_variable_map.serialize_json(
                value["environment_variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutGraphqlApiEnvironmentVariablesResponse:
    out: PutGraphqlApiEnvironmentVariablesResponse = {}  # type: ignore[typeddict-item]
    if "environmentVariables" in data:
        import aws_sdk_appsync.types.environment_variable_map

        out["environment_variables"] = (
            aws_sdk_appsync.types.environment_variable_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    return out
