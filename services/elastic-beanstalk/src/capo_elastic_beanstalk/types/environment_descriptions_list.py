"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentDescriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_description

EnvironmentDescriptionsList: TypeAlias = list[
    "capo_elastic_beanstalk.types.environment_description.EnvironmentDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentDescriptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.environment_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.environment_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EnvironmentDescriptionsList:
    import capo_elastic_beanstalk.types.environment_description

    out: EnvironmentDescriptionsList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.environment_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: EnvironmentDescriptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.environment_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.environment_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EnvironmentDescriptionsList:
    import capo_elastic_beanstalk.types.environment_description

    out: EnvironmentDescriptionsList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.environment_description.deserialize_query(
                child
            )
        )
    return out
