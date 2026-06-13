"""Generated from Smithy shape ``com.amazonaws.proton#AcceptEnvironmentAccountConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection_id


class AcceptEnvironmentAccountConnectionInput(TypedDict):
    id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
    """<p>The ID of the environment account connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptEnvironmentAccountConnectionInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptEnvironmentAccountConnectionInput:
    out: AcceptEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "AcceptEnvironmentAccountConnectionInput.id required"
        )
    return out
