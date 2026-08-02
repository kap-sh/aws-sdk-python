"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionModifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.load_permission_list_request


class LoadPermissionModifications(TypedDict, closed=True):
    add: NotRequired[
        "capo_ec2.types.load_permission_list_request.LoadPermissionListRequest"
    ]
    """<p>The load permissions to add.</p>"""
    remove: NotRequired[
        "capo_ec2.types.load_permission_list_request.LoadPermissionListRequest"
    ]
    """<p>The load permissions to remove.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadPermissionModifications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "add" in value:
        import capo_ec2.types.load_permission_list_request

        capo_ec2.types.load_permission_list_request.serialize_ec2_query(
            value["add"], pairs, f"{key_prefix}Add"
        )
    if "remove" in value:
        import capo_ec2.types.load_permission_list_request

        capo_ec2.types.load_permission_list_request.serialize_ec2_query(
            value["remove"], pairs, f"{key_prefix}Remove"
        )


def deserialize_ec2_query(el: Element) -> LoadPermissionModifications:
    out: LoadPermissionModifications = {}  # type: ignore[typeddict-item]
    if el.find("Add") is not None:
        import capo_ec2.types.load_permission_list_request

        out["add"] = capo_ec2.types.load_permission_list_request.deserialize_ec2_query(
            el, "Add"
        )
    if el.find("Remove") is not None:
        import capo_ec2.types.load_permission_list_request

        out["remove"] = (
            capo_ec2.types.load_permission_list_request.deserialize_ec2_query(
                el, "Remove"
            )
        )
    return out
