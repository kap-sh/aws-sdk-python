"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSessionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_session_field

TrafficMirrorSessionFieldList: TypeAlias = list[
    "capo_ec2.types.traffic_mirror_session_field.TrafficMirrorSessionField"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorSessionFieldList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.traffic_mirror_session_field

        capo_ec2.types.traffic_mirror_session_field.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TrafficMirrorSessionFieldList:
    import capo_ec2.types.traffic_mirror_session_field

    out: TrafficMirrorSessionFieldList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.traffic_mirror_session_field.deserialize_ec2_query(child)
        )
    return out
