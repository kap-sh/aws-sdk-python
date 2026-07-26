"""Generated from Smithy shape ``com.amazonaws.s3control#Scope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.prefixes_list
    import capo_s3_control.types.scope_permission_list


class Scope(TypedDict, closed=True):
    prefixes: NotRequired["capo_s3_control.types.prefixes_list.PrefixesList"]
    """<p>You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.</p>"""
    permissions: NotRequired[
        "capo_s3_control.types.scope_permission_list.ScopePermissionList"
    ]
    """<p>You can include one or more API operations as permissions.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Scope, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefixes" in value:
        import capo_s3_control.types.prefixes_list

        capo_s3_control.types.prefixes_list.serialize_xml(
            value["prefixes"], el, "Prefixes"
        )
    if "permissions" in value:
        import capo_s3_control.types.scope_permission_list

        capo_s3_control.types.scope_permission_list.serialize_xml(
            value["permissions"], el, "Permissions"
        )


def deserialize_xml(el: Element) -> Scope:
    out: Scope = {}  # type: ignore[typeddict-item]
    child_prefixes = el.find("Prefixes")
    if child_prefixes is not None:
        import capo_s3_control.types.prefixes_list

        out["prefixes"] = capo_s3_control.types.prefixes_list.deserialize_xml(
            child_prefixes
        )
    child_permissions = el.find("Permissions")
    if child_permissions is not None:
        import capo_s3_control.types.scope_permission_list

        out["permissions"] = (
            capo_s3_control.types.scope_permission_list.deserialize_xml(
                child_permissions
            )
        )
    return out
