"""Generated from Smithy shape ``com.amazonaws.ses#EventDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.event_destination

EventDestinations: TypeAlias = list[
    "aws_sdk_ses.types.event_destination.EventDestination"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventDestinations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.event_destination

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.event_destination.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EventDestinations:
    import aws_sdk_ses.types.event_destination

    out: EventDestinations = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.event_destination.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EventDestinations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.event_destination

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.event_destination.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EventDestinations:
    import aws_sdk_ses.types.event_destination

    out: EventDestinations = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.event_destination.deserialize_query(child))
    return out
