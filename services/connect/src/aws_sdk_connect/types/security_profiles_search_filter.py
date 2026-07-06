"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfilesSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.control_plane_tag_filter


class SecurityProfilesSearchFilter(TypedDict, closed=True):
    tag_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfilesSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["TagFilter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.serialize_json(
                value["tag_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityProfilesSearchFilter:
    out: SecurityProfilesSearchFilter = {}  # type: ignore[typeddict-item]
    if "TagFilter" in data:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    return out
