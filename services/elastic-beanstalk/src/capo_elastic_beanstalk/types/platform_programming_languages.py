"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformProgrammingLanguages``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_programming_language

PlatformProgrammingLanguages: TypeAlias = list[
    "capo_elastic_beanstalk.types.platform_programming_language.PlatformProgrammingLanguage"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformProgrammingLanguages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.platform_programming_language

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.platform_programming_language.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PlatformProgrammingLanguages:
    import capo_elastic_beanstalk.types.platform_programming_language

    out: PlatformProgrammingLanguages = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.platform_programming_language.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PlatformProgrammingLanguages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.platform_programming_language

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.platform_programming_language.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PlatformProgrammingLanguages:
    import capo_elastic_beanstalk.types.platform_programming_language

    out: PlatformProgrammingLanguages = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.platform_programming_language.deserialize_query(
                child
            )
        )
    return out
