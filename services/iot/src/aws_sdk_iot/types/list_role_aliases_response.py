"""Generated from Smithy shape ``com.amazonaws.iot#ListRoleAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.role_aliases


class ListRoleAliasesResponse(TypedDict, closed=True):
    role_aliases: NotRequired["aws_sdk_iot.types.role_aliases.RoleAliases"]
    """<p>The role aliases.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoleAliasesResponse) -> dict:
    out: dict = {}
    if "role_aliases" in value:
        import aws_sdk_iot.types.role_aliases

        out["roleAliases"] = aws_sdk_iot.types.role_aliases.serialize_json(
            value["role_aliases"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListRoleAliasesResponse:
    out: ListRoleAliasesResponse = {}  # type: ignore[typeddict-item]
    if "roleAliases" in data:
        import aws_sdk_iot.types.role_aliases

        out["role_aliases"] = aws_sdk_iot.types.role_aliases.deserialize_json(
            data["roleAliases"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
