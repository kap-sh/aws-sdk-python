"""Generated from Smithy shape ``com.amazonaws.proton#AcceptEnvironmentAccountConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection


class AcceptEnvironmentAccountConnectionOutput(TypedDict, closed=True):
    environment_account_connection: (
        "capo_proton.types.environment_account_connection.EnvironmentAccountConnection"
    )
    """<p>The environment account connection data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptEnvironmentAccountConnectionOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_account_connection

    out["environmentAccountConnection"] = (
        capo_proton.types.environment_account_connection.serialize_aws_json_1_0(
            value["environment_account_connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptEnvironmentAccountConnectionOutput:
    out: AcceptEnvironmentAccountConnectionOutput = {}  # type: ignore[typeddict-item]
    if "environmentAccountConnection" in data:
        import capo_proton.types.environment_account_connection

        out["environment_account_connection"] = (
            capo_proton.types.environment_account_connection.deserialize_aws_json_1_0(
                data["environmentAccountConnection"]
            )
        )
    else:
        raise DeserializationError(
            "AcceptEnvironmentAccountConnectionOutput.environment_account_connection required"
        )
    return out
