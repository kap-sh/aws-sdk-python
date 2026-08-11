"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.access_scope_path

AccessScopePathList: TypeAlias = list[
    "capo_ec2.types.access_scope_path.AccessScopePath"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePathList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.access_scope_path

        capo_ec2.types.access_scope_path.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AccessScopePathList:
    import capo_ec2.types.access_scope_path

    out: AccessScopePathList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.access_scope_path.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AccessScopePathList:
    import capo_ec2.types.access_scope_path

    out: AccessScopePathList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.access_scope_path.deserialize_ec2_query(child))
    return out
