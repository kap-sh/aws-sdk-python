"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_description

ApplicationDescriptionList: TypeAlias = list[
    "capo_elastic_beanstalk.types.application_description.ApplicationDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.application_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.application_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ApplicationDescriptionList:
    import capo_elastic_beanstalk.types.application_description

    out: ApplicationDescriptionList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.application_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ApplicationDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.application_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.application_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ApplicationDescriptionList:
    import capo_elastic_beanstalk.types.application_description

    out: ApplicationDescriptionList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.application_description.deserialize_query(
                child
            )
        )
    return out
