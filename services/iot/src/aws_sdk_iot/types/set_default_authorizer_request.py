"""Generated from Smithy shape ``com.amazonaws.iot#SetDefaultAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_name


class SetDefaultAuthorizerRequest(TypedDict, closed=True):
    authorizer_name: "aws_sdk_iot.types.authorizer_name.AuthorizerName"
    """<p>The authorizer name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDefaultAuthorizerRequest) -> dict:
    out: dict = {}
    out["authorizerName"] = value["authorizer_name"]
    return out


def deserialize_json(data: dict) -> SetDefaultAuthorizerRequest:
    out: SetDefaultAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if "authorizerName" in data:
        out["authorizer_name"] = data["authorizerName"]
    else:
        raise DeserializationError(
            "SetDefaultAuthorizerRequest.authorizer_name required"
        )
    return out
