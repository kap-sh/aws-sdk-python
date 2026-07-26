"""Generated from Smithy shape ``com.amazonaws.redshift#RevisionTargetsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.revision_target

RevisionTargetsList: TypeAlias = list[
    "capo_redshift.types.revision_target.RevisionTarget"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RevisionTargetsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.revision_target

    for n, item in enumerate(value, 1):
        capo_redshift.types.revision_target.serialize_query(
            item, pairs, f"{prefix}.RevisionTarget.{n}"
        )


def deserialize_query(el: Element) -> RevisionTargetsList:
    import capo_redshift.types.revision_target

    out: RevisionTargetsList = []
    for child in el.findall("RevisionTarget"):
        out.append(capo_redshift.types.revision_target.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RevisionTargetsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.revision_target

    for n, item in enumerate(value, 1):
        capo_redshift.types.revision_target.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RevisionTargetsList:
    import capo_redshift.types.revision_target

    out: RevisionTargetsList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.revision_target.deserialize_query(child))
    return out
