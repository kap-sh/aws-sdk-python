"""Generated from Smithy shape ``com.amazonaws.sns#SubscriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.subscription

SubscriptionsList: TypeAlias = list["aws_sdk_sns.types.subscription.Subscription"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubscriptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.subscription

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.subscription.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SubscriptionsList:
    import aws_sdk_sns.types.subscription

    out: SubscriptionsList = []
    for child in el.findall("member"):
        out.append(aws_sdk_sns.types.subscription.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SubscriptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.subscription

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.subscription.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SubscriptionsList:
    import aws_sdk_sns.types.subscription

    out: SubscriptionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sns.types.subscription.deserialize_query(child))
    return out
