"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AutoScalingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.auto_scaling_group

AutoScalingGroupList: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.auto_scaling_group.AutoScalingGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.auto_scaling_group

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.auto_scaling_group.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AutoScalingGroupList:
    import aws_sdk_elastic_beanstalk.types.auto_scaling_group

    out: AutoScalingGroupList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.auto_scaling_group.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AutoScalingGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.auto_scaling_group

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.auto_scaling_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AutoScalingGroupList:
    import aws_sdk_elastic_beanstalk.types.auto_scaling_group

    out: AutoScalingGroupList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.auto_scaling_group.deserialize_query(child)
        )
    return out
