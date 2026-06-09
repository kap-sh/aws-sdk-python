"""Generated from Smithy shape ``com.amazonaws.ec2#SubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subscription

SubscriptionList: TypeAlias = list["aws_sdk_ec2.types.subscription.Subscription"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubscriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.subscription

        aws_sdk_ec2.types.subscription.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> SubscriptionList:
    import aws_sdk_ec2.types.subscription

    out: SubscriptionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.subscription.deserialize_ec2_query(child))
    return out
