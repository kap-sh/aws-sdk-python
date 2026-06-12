"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateAccessTokenOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short


class UpdateAccessTokenOutput(TypedDict):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the token.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    """<p>The name of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessTokenOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateAccessTokenOutput:
    out: UpdateAccessTokenOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateAccessTokenOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAccessTokenOutput.name required")
    return out
