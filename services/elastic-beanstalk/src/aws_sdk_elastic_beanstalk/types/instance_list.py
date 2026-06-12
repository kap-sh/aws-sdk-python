"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.instance

InstanceList: TypeAlias = list["aws_sdk_elastic_beanstalk.types.instance.Instance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.instance

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.instance.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstanceList:
    import aws_sdk_elastic_beanstalk.types.instance

    out: InstanceList = []
    for child in el.findall("member"):
        out.append(aws_sdk_elastic_beanstalk.types.instance.deserialize_query(child))
    return out


def serialize_query_flat(
    value: InstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.instance

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.instance.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstanceList:
    import aws_sdk_elastic_beanstalk.types.instance

    out: InstanceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elastic_beanstalk.types.instance.deserialize_query(child))
    return out
