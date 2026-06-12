"""Generated from Smithy shape ``com.amazonaws.cloudformation#RollbackTriggers``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.rollback_trigger

RollbackTriggers: TypeAlias = list[
    "aws_sdk_cloudformation.types.rollback_trigger.RollbackTrigger"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RollbackTriggers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.rollback_trigger

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.rollback_trigger.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RollbackTriggers:
    import aws_sdk_cloudformation.types.rollback_trigger

    out: RollbackTriggers = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.rollback_trigger.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RollbackTriggers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.rollback_trigger

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.rollback_trigger.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RollbackTriggers:
    import aws_sdk_cloudformation.types.rollback_trigger

    out: RollbackTriggers = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.rollback_trigger.deserialize_query(child)
        )
    return out
