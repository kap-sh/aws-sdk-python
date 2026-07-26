"""Generated from Smithy shape ``com.amazonaws.autoscaling#NotificationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.notification_configuration

NotificationConfigurations: TypeAlias = list[
    "capo_auto_scaling.types.notification_configuration.NotificationConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NotificationConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.notification_configuration

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.notification_configuration.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> NotificationConfigurations:
    import capo_auto_scaling.types.notification_configuration

    out: NotificationConfigurations = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.notification_configuration.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: NotificationConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.notification_configuration

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.notification_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NotificationConfigurations:
    import capo_auto_scaling.types.notification_configuration

    out: NotificationConfigurations = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.notification_configuration.deserialize_query(child)
        )
    return out
