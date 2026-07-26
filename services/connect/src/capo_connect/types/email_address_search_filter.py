"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.control_plane_tag_filter


class EmailAddressSearchFilter(TypedDict, closed=True):
    tag_filter: NotRequired[
        "capo_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import capo_connect.types.control_plane_tag_filter

        out["TagFilter"] = capo_connect.types.control_plane_tag_filter.serialize_json(
            value["tag_filter"]
        )
    return out


def deserialize_json(data: dict) -> EmailAddressSearchFilter:
    out: EmailAddressSearchFilter = {}  # type: ignore[typeddict-item]
    if "TagFilter" in data:
        import capo_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            capo_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    return out
