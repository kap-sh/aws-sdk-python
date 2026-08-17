"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.access_scope_path_request

AccessScopePathListRequest: TypeAlias = list[
    "capo_ec2.types.access_scope_path_request.AccessScopePathRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePathListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.access_scope_path_request

        capo_ec2.types.access_scope_path_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AccessScopePathListRequest:
    import capo_ec2.types.access_scope_path_request

    out: AccessScopePathListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.access_scope_path_request.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AccessScopePathListRequest:
    import capo_ec2.types.access_scope_path_request

    out: AccessScopePathListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.access_scope_path_request.deserialize_ec2_query(child)
        )
    return out
