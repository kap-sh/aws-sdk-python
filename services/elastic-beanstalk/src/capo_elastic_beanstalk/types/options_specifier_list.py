"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#OptionsSpecifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.option_specification

OptionsSpecifierList: TypeAlias = list[
    "capo_elastic_beanstalk.types.option_specification.OptionSpecification"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionsSpecifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.option_specification

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.option_specification.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> OptionsSpecifierList:
    import capo_elastic_beanstalk.types.option_specification

    out: OptionsSpecifierList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.option_specification.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: OptionsSpecifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.option_specification

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.option_specification.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OptionsSpecifierList:
    import capo_elastic_beanstalk.types.option_specification

    out: OptionsSpecifierList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.option_specification.deserialize_query(child)
        )
    return out
