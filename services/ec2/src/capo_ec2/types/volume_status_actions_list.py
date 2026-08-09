"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.volume_status_action

VolumeStatusActionsList: TypeAlias = list[
    "capo_ec2.types.volume_status_action.VolumeStatusAction"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusActionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.volume_status_action

        capo_ec2.types.volume_status_action.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VolumeStatusActionsList:
    import capo_ec2.types.volume_status_action

    out: VolumeStatusActionsList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.volume_status_action.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VolumeStatusActionsList:
    import capo_ec2.types.volume_status_action

    out: VolumeStatusActionsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.volume_status_action.deserialize_ec2_query(child))
    return out
