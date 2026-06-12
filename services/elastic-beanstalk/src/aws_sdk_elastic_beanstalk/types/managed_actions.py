"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ManagedActions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.managed_action

ManagedActions: TypeAlias = list[
    "aws_sdk_elastic_beanstalk.types.managed_action.ManagedAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.managed_action

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.managed_action.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ManagedActions:
    import aws_sdk_elastic_beanstalk.types.managed_action

    out: ManagedActions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_beanstalk.types.managed_action.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ManagedActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_beanstalk.types.managed_action

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_beanstalk.types.managed_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ManagedActions:
    import aws_sdk_elastic_beanstalk.types.managed_action

    out: ManagedActions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_beanstalk.types.managed_action.deserialize_query(child)
        )
    return out
