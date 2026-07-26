"""Generated from Smithy shape ``com.amazonaws.quicksight#LinkSharingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_permission_list


class LinkSharingConfiguration(TypedDict, closed=True):
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A structure that contains the permissions of a shareable link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkSharingConfiguration) -> dict:
    out: dict = {}
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinkSharingConfiguration:
    out: LinkSharingConfiguration = {}  # type: ignore[typeddict-item]
    if "Permissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    return out
