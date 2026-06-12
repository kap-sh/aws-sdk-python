"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentInfoDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_info_description

EnvironmentInfoDescriptionList: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.environment_info_description.EnvironmentInfoDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentInfoDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.environment_info_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.environment_info_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EnvironmentInfoDescriptionList:
    import aws_sdk_elastic_beanstalk.types.environment_info_description

    out: EnvironmentInfoDescriptionList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.environment_info_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: EnvironmentInfoDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.environment_info_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.environment_info_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EnvironmentInfoDescriptionList:
    import aws_sdk_elastic_beanstalk.types.environment_info_description

    out: EnvironmentInfoDescriptionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.environment_info_description.deserialize_query(
                child
            )
        )
    return out
