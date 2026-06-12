"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentHealthAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_health_attribute

EnvironmentHealthAttributes: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.environment_health_attribute.EnvironmentHealthAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentHealthAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.environment_health_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.environment_health_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EnvironmentHealthAttributes:
    import aws_sdk_elastic_beanstalk.types.environment_health_attribute

    out: EnvironmentHealthAttributes = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.environment_health_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: EnvironmentHealthAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.environment_health_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.environment_health_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EnvironmentHealthAttributes:
    import aws_sdk_elastic_beanstalk.types.environment_health_attribute

    out: EnvironmentHealthAttributes = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.environment_health_attribute.deserialize_query(
                child
            )
        )
    return out
