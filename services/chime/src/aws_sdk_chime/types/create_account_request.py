"""Generated from Smithy shape ``com.amazonaws.chime#CreateAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.account_name


class CreateAccountRequest(TypedDict, closed=True):
    name: "aws_sdk_chime.types.account_name.AccountName"
    """<p>The name of the Amazon Chime account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateAccountRequest:
    out: CreateAccountRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAccountRequest.name required")
    return out
