"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentAccountConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection_id


class DeleteEnvironmentAccountConnectionInput(TypedDict, closed=True):
    id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentAccountConnectionInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentAccountConnectionInput:
    out: DeleteEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "DeleteEnvironmentAccountConnectionInput.id required"
        )
    return out
