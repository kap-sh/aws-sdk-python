"""Generated from Smithy shape ``com.amazonaws.medialive#InputSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputSourceRequest(TypedDict, closed=True):
    password_param: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The key used to extract the password from EC2 Parameter store."""
    url: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """This represents the customer's source URL where stream is pulled from."""
    username: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The username for the input source."""


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceRequest) -> dict:
    out: dict = {}
    if "password_param" in value:
        out["passwordParam"] = value["password_param"]
    if "url" in value:
        out["url"] = value["url"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> InputSourceRequest:
    out: InputSourceRequest = {}  # type: ignore[typeddict-item]
    if "passwordParam" in data:
        out["password_param"] = data["passwordParam"]
    if "url" in data:
        out["url"] = data["url"]
    if "username" in data:
        out["username"] = data["username"]
    return out
