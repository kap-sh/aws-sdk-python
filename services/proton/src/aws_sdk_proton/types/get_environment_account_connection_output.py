"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentAccountConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection


class GetEnvironmentAccountConnectionOutput(TypedDict, closed=True):
    environment_account_connection: "aws_sdk_proton.types.environment_account_connection.EnvironmentAccountConnection"
    """<p>The detailed data of the requested environment account connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentAccountConnectionOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.environment_account_connection

    out["environmentAccountConnection"] = (
        aws_sdk_proton.types.environment_account_connection.serialize_aws_json_1_0(
            value["environment_account_connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentAccountConnectionOutput:
    out: GetEnvironmentAccountConnectionOutput = {}  # type: ignore[typeddict-item]
    if "environmentAccountConnection" in data:
        import aws_sdk_proton.types.environment_account_connection

        out["environment_account_connection"] = (
            aws_sdk_proton.types.environment_account_connection.deserialize_aws_json_1_0(
                data["environmentAccountConnection"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnvironmentAccountConnectionOutput.environment_account_connection required"
        )
    return out
