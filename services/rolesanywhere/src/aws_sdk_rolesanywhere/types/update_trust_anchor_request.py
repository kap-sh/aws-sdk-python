"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UpdateTrustAnchorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.resource_name
    import aws_sdk_rolesanywhere.types.source
    import aws_sdk_rolesanywhere.types.uuid


class UpdateTrustAnchorRequest(TypedDict):
    trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the trust anchor.</p>"""
    name: NotRequired["aws_sdk_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the trust anchor.</p>"""
    source: NotRequired["aws_sdk_rolesanywhere.types.source.Source"]
    """<p>The trust anchor type and its related certificate data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTrustAnchorRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "source" in value:
        import aws_sdk_rolesanywhere.types.source

        out["source"] = aws_sdk_rolesanywhere.types.source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTrustAnchorRequest:
    out: UpdateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "source" in data:
        import aws_sdk_rolesanywhere.types.source

        out["source"] = aws_sdk_rolesanywhere.types.source.deserialize_json(
            data["source"]
        )
    return out
