"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.connection_notification

ConnectionNotificationSet: TypeAlias = list[
    "capo_ec2.types.connection_notification.ConnectionNotification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConnectionNotificationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.connection_notification

        capo_ec2.types.connection_notification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ConnectionNotificationSet:
    import capo_ec2.types.connection_notification

    out: ConnectionNotificationSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.connection_notification.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ConnectionNotificationSet:
    import capo_ec2.types.connection_notification

    out: ConnectionNotificationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.connection_notification.deserialize_ec2_query(child))
    return out
