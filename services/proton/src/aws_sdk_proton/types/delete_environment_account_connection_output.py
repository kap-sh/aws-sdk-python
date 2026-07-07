"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentAccountConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection


class DeleteEnvironmentAccountConnectionOutput(TypedDict, closed=True):
    environment_account_connection: NotRequired[
        "aws_sdk_proton.types.environment_account_connection.EnvironmentAccountConnection"
    ]
    """<p>The detailed data of the environment account connection being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentAccountConnectionOutput) -> dict:
    out: dict = {}
    if "environment_account_connection" in value:
        import aws_sdk_proton.types.environment_account_connection

        out["environmentAccountConnection"] = (
            aws_sdk_proton.types.environment_account_connection.serialize_aws_json_1_0(
                value["environment_account_connection"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentAccountConnectionOutput:
    out: DeleteEnvironmentAccountConnectionOutput = {}  # type: ignore[typeddict-item]
    if "environmentAccountConnection" in data:
        import aws_sdk_proton.types.environment_account_connection

        out["environment_account_connection"] = (
            aws_sdk_proton.types.environment_account_connection.deserialize_aws_json_1_0(
                data["environmentAccountConnection"]
            )
        )
    return out
