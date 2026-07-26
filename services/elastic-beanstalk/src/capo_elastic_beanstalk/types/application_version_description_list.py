"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_version_description

ApplicationVersionDescriptionList: TypeAlias = list[
    "capo_elastic_beanstalk.types.application_version_description.ApplicationVersionDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationVersionDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.application_version_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.application_version_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ApplicationVersionDescriptionList:
    import capo_elastic_beanstalk.types.application_version_description

    out: ApplicationVersionDescriptionList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.application_version_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ApplicationVersionDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.application_version_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.application_version_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ApplicationVersionDescriptionList:
    import capo_elastic_beanstalk.types.application_version_description

    out: ApplicationVersionDescriptionList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.application_version_description.deserialize_query(
                child
            )
        )
    return out
