"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EventDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.event_description

EventDescriptionList: TypeAlias = list[
    "capo_elastic_beanstalk.types.event_description.EventDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EventDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.event_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.event_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EventDescriptionList:
    import capo_elastic_beanstalk.types.event_description

    out: EventDescriptionList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.event_description.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: EventDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.event_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.event_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EventDescriptionList:
    import capo_elastic_beanstalk.types.event_description

    out: EventDescriptionList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.event_description.deserialize_query(child)
        )
    return out
