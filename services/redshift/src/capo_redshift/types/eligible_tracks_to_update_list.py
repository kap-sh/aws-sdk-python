"""Generated from Smithy shape ``com.amazonaws.redshift#EligibleTracksToUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.update_target

EligibleTracksToUpdateList: TypeAlias = list[
    "capo_redshift.types.update_target.UpdateTarget"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EligibleTracksToUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.update_target

    for n, item in enumerate(value, 1):
        capo_redshift.types.update_target.serialize_query(
            item, pairs, f"{prefix}.UpdateTarget.{n}"
        )


def deserialize_query(el: Element) -> EligibleTracksToUpdateList:
    import capo_redshift.types.update_target

    out: EligibleTracksToUpdateList = []
    for child in el.findall("UpdateTarget"):
        out.append(capo_redshift.types.update_target.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EligibleTracksToUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.update_target

    for n, item in enumerate(value, 1):
        capo_redshift.types.update_target.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EligibleTracksToUpdateList:
    import capo_redshift.types.update_target

    out: EligibleTracksToUpdateList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.update_target.deserialize_query(child))
    return out
