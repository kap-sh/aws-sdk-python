"""Generated from Smithy shape ``com.amazonaws.proton#UpdateEnvironmentAccountConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection


class UpdateEnvironmentAccountConnectionOutput(TypedDict, closed=True):
    environment_account_connection: (
        "capo_proton.types.environment_account_connection.EnvironmentAccountConnection"
    )
    """<p>The environment account connection detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentAccountConnectionOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_account_connection

    out["environmentAccountConnection"] = (
        capo_proton.types.environment_account_connection.serialize_aws_json_1_0(
            value["environment_account_connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentAccountConnectionOutput:
    out: UpdateEnvironmentAccountConnectionOutput = {}  # type: ignore[typeddict-item]
    if "environmentAccountConnection" in data:
        import capo_proton.types.environment_account_connection

        out["environment_account_connection"] = (
            capo_proton.types.environment_account_connection.deserialize_aws_json_1_0(
                data["environmentAccountConnection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnvironmentAccountConnectionOutput.environment_account_connection required"
        )
    return out
