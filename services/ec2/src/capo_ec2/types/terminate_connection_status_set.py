"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateConnectionStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.terminate_connection_status

TerminateConnectionStatusSet: TypeAlias = list[
    "capo_ec2.types.terminate_connection_status.TerminateConnectionStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateConnectionStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.terminate_connection_status

        capo_ec2.types.terminate_connection_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TerminateConnectionStatusSet:
    import capo_ec2.types.terminate_connection_status

    out: TerminateConnectionStatusSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.terminate_connection_status.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TerminateConnectionStatusSet:
    import capo_ec2.types.terminate_connection_status

    out: TerminateConnectionStatusSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.terminate_connection_status.deserialize_ec2_query(child)
        )
    return out
