"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kx_environment_name


class UpdateKxEnvironmentRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    name: NotRequired["aws_sdk_finspace.types.kx_environment_name.KxEnvironmentName"]
    """<p>The name of the kdb environment.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the kdb environment.</p>"""
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxEnvironmentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxEnvironmentRequest:
    out: UpdateKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
