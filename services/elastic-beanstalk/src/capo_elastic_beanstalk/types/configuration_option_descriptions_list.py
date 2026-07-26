"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionDescriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.configuration_option_description

ConfigurationOptionDescriptionsList: TypeAlias = list[
    "capo_elastic_beanstalk.types.configuration_option_description.ConfigurationOptionDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationOptionDescriptionsList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elastic_beanstalk.types.configuration_option_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.configuration_option_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ConfigurationOptionDescriptionsList:
    import capo_elastic_beanstalk.types.configuration_option_description

    out: ConfigurationOptionDescriptionsList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.configuration_option_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ConfigurationOptionDescriptionsList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elastic_beanstalk.types.configuration_option_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.configuration_option_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ConfigurationOptionDescriptionsList:
    import capo_elastic_beanstalk.types.configuration_option_description

    out: ConfigurationOptionDescriptionsList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.configuration_option_description.deserialize_query(
                child
            )
        )
    return out
