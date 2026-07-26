"""Generated from Smithy shape ``com.amazonaws.connect#ViewSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.control_plane_attribute_filter


class ViewSearchFilter(TypedDict, closed=True):
    attribute_filter: NotRequired[
        "capo_connect.types.control_plane_attribute_filter.ControlPlaneAttributeFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ViewSearchFilter) -> dict:
    out: dict = {}
    if "attribute_filter" in value:
        import capo_connect.types.control_plane_attribute_filter

        out["AttributeFilter"] = (
            capo_connect.types.control_plane_attribute_filter.serialize_json(
                value["attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ViewSearchFilter:
    out: ViewSearchFilter = {}  # type: ignore[typeddict-item]
    if "AttributeFilter" in data:
        import capo_connect.types.control_plane_attribute_filter

        out["attribute_filter"] = (
            capo_connect.types.control_plane_attribute_filter.deserialize_json(
                data["AttributeFilter"]
            )
        )
    return out
