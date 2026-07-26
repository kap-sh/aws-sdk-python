"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformFrameworks``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_framework

PlatformFrameworks: TypeAlias = list[
    "capo_elastic_beanstalk.types.platform_framework.PlatformFramework"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformFrameworks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.platform_framework

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.platform_framework.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PlatformFrameworks:
    import capo_elastic_beanstalk.types.platform_framework

    out: PlatformFrameworks = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.platform_framework.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PlatformFrameworks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.platform_framework

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.platform_framework.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PlatformFrameworks:
    import capo_elastic_beanstalk.types.platform_framework

    out: PlatformFrameworks = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.platform_framework.deserialize_query(child)
        )
    return out
