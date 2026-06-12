"""Generated from Smithy shape ``com.amazonaws.autoscaling#NotificationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.notification_configuration

NotificationConfigurations: TypeAlias = list[
    "aws_sdk_auto_scaling.types.notification_configuration.NotificationConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NotificationConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.notification_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.notification_configuration.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> NotificationConfigurations:
    import aws_sdk_auto_scaling.types.notification_configuration

    out: NotificationConfigurations = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.notification_configuration.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: NotificationConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.notification_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.notification_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NotificationConfigurations:
    import aws_sdk_auto_scaling.types.notification_configuration

    out: NotificationConfigurations = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.notification_configuration.deserialize_query(
                child
            )
        )
    return out
