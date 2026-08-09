"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.load_permission_request

LoadPermissionListRequest: TypeAlias = list[
    "capo_ec2.types.load_permission_request.LoadPermissionRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadPermissionListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.load_permission_request

        capo_ec2.types.load_permission_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LoadPermissionListRequest:
    import capo_ec2.types.load_permission_request

    out: LoadPermissionListRequest = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.load_permission_request.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LoadPermissionListRequest:
    import capo_ec2.types.load_permission_request

    out: LoadPermissionListRequest = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.load_permission_request.deserialize_ec2_query(child))
    return out
