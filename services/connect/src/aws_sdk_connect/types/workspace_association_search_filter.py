"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceAssociationSearchFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.control_plane_attribute_filter


class WorkspaceAssociationSearchFilter(TypedDict):
    attribute_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_attribute_filter.ControlPlaneAttributeFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceAssociationSearchFilter) -> dict:
    out: dict = {}
    if "attribute_filter" in value:
        import aws_sdk_connect.types.control_plane_attribute_filter

        out["AttributeFilter"] = (
            aws_sdk_connect.types.control_plane_attribute_filter.serialize_json(
                value["attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkspaceAssociationSearchFilter:
    out: WorkspaceAssociationSearchFilter = {}  # type: ignore[typeddict-item]
    if "AttributeFilter" in data:
        import aws_sdk_connect.types.control_plane_attribute_filter

        out["attribute_filter"] = (
            aws_sdk_connect.types.control_plane_attribute_filter.deserialize_json(
                data["AttributeFilter"]
            )
        )
    return out
