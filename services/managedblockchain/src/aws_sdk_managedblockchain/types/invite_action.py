"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InviteAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.principal_string


class InviteAction(TypedDict, closed=True):
    principal: "aws_sdk_managedblockchain.types.principal_string.PrincipalString"
    """<p>The Amazon Web Services account ID to invite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteAction) -> dict:
    out: dict = {}
    out["Principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> InviteAction:
    out: InviteAction = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        out["principal"] = data["Principal"]
    else:
        raise DeserializationError("InviteAction.principal required")
    return out
