"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ManagedActionHistoryItems``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.managed_action_history_item

ManagedActionHistoryItems: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.managed_action_history_item.ManagedActionHistoryItem"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedActionHistoryItems, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.managed_action_history_item

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.managed_action_history_item.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ManagedActionHistoryItems:
    import aws_sdk_elastic_beanstalk.types.managed_action_history_item

    out: ManagedActionHistoryItems = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.managed_action_history_item.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ManagedActionHistoryItems, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.managed_action_history_item

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.managed_action_history_item.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ManagedActionHistoryItems:
    import aws_sdk_elastic_beanstalk.types.managed_action_history_item

    out: ManagedActionHistoryItems = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.managed_action_history_item.deserialize_query(
                child
            )
        )
    return out
