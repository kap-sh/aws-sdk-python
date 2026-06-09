"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotificationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification

ConnectionNotificationSet: TypeAlias = list[
    "aws_sdk_ec2.types.connection_notification.ConnectionNotification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConnectionNotificationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.connection_notification

        aws_sdk_ec2.types.connection_notification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ConnectionNotificationSet:
    import aws_sdk_ec2.types.connection_notification

    out: ConnectionNotificationSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.connection_notification.deserialize_ec2_query(child)
        )
    return out
