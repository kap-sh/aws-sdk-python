"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LaunchTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.launch_template

LaunchTemplateList: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.launch_template.LaunchTemplate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchTemplateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.launch_template

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.launch_template.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LaunchTemplateList:
    import aws_sdk_elastic_beanstalk.types.launch_template

    out: LaunchTemplateList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.launch_template.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: LaunchTemplateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.launch_template

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.launch_template.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LaunchTemplateList:
    import aws_sdk_elastic_beanstalk.types.launch_template

    out: LaunchTemplateList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.launch_template.deserialize_query(child)
        )
    return out
