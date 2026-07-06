"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateAccessTokenInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short


class UpdateAccessTokenInput(TypedDict, closed=True):
    access_token_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the token.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    """<p>The new name of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessTokenInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAccessTokenInput:
    out: UpdateAccessTokenInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAccessTokenInput.name required")
    return out
