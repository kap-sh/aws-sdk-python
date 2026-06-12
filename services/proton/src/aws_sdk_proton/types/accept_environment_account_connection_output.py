"""Generated from Smithy shape ``com.amazonaws.proton#AcceptEnvironmentAccountConnectionOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_proton.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection

class AcceptEnvironmentAccountConnectionOutput(TypedDict):
    environment_account_connection: "aws_sdk_proton.types.environment_account_connection.EnvironmentAccountConnection"
    """<p>The environment account connection data that's returned by Proton.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptEnvironmentAccountConnectionOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.environment_account_connection
    out["environmentAccountConnection"] = aws_sdk_proton.types.environment_account_connection.serialize_aws_json_1_0(value["environment_account_connection"])
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptEnvironmentAccountConnectionOutput:
    out: AcceptEnvironmentAccountConnectionOutput = {}  # type: ignore[typeddict-item]
    if "environmentAccountConnection" in data:
        import aws_sdk_proton.types.environment_account_connection
        out["environment_account_connection"] = aws_sdk_proton.types.environment_account_connection.deserialize_aws_json_1_0(data["environmentAccountConnection"])
    else:
        raise DeserializationError("AcceptEnvironmentAccountConnectionOutput.environment_account_connection required")
    return out