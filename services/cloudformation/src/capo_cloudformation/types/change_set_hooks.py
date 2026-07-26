"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHooks``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_hook

ChangeSetHooks: TypeAlias = list[
    "capo_cloudformation.types.change_set_hook.ChangeSetHook"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetHooks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.change_set_hook

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.change_set_hook.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ChangeSetHooks:
    import capo_cloudformation.types.change_set_hook

    out: ChangeSetHooks = []
    for child in el.findall("member"):
        out.append(capo_cloudformation.types.change_set_hook.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ChangeSetHooks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.change_set_hook

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.change_set_hook.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ChangeSetHooks:
    import capo_cloudformation.types.change_set_hook

    out: ChangeSetHooks = []
    for child in parent.findall(tag):
        out.append(capo_cloudformation.types.change_set_hook.deserialize_query(child))
    return out
