"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentLinks``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_link

EnvironmentLinks: TypeAlias = list[
    "capo_elastic_beanstalk.types.environment_link.EnvironmentLink"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentLinks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.environment_link

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.environment_link.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EnvironmentLinks:
    import capo_elastic_beanstalk.types.environment_link

    out: EnvironmentLinks = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.environment_link.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: EnvironmentLinks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.environment_link

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.environment_link.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EnvironmentLinks:
    import capo_elastic_beanstalk.types.environment_link

    out: EnvironmentLinks = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.environment_link.deserialize_query(child)
        )
    return out
