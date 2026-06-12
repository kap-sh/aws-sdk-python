"""Generated from Smithy shape ``com.amazonaws.medialive#InputLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_max2048


class InputLocation(TypedDict):
    password_param: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """key used to extract the password from EC2 Parameter store"""
    uri: NotRequired["aws_sdk_medialive.types.__string_max2048.__stringMax2048"]
    """Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: \"rtmp://fmsserver/live\"."""
    username: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Documentation update needed"""


# --- restJson1 ser/de ---
def serialize_json(value: InputLocation) -> dict:
    out: dict = {}
    if "password_param" in value:
        out["passwordParam"] = value["password_param"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> InputLocation:
    out: InputLocation = {}  # type: ignore[typeddict-item]
    if "passwordParam" in data:
        out["password_param"] = data["passwordParam"]
    if "uri" in data:
        out["uri"] = data["uri"]
    if "username" in data:
        out["username"] = data["username"]
    return out
