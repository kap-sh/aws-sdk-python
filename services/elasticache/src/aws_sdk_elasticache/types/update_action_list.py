"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.update_action

UpdateActionList: TypeAlias = list[
    "aws_sdk_elasticache.types.update_action.UpdateAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.update_action

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.update_action.serialize_query(
            item, pairs, f"{prefix}.UpdateAction.{n}"
        )


def deserialize_query(el: Element) -> UpdateActionList:
    import aws_sdk_elasticache.types.update_action

    out: UpdateActionList = []
    for child in el.findall("UpdateAction"):
        out.append(aws_sdk_elasticache.types.update_action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.update_action

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.update_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UpdateActionList:
    import aws_sdk_elasticache.types.update_action

    out: UpdateActionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.update_action.deserialize_query(child))
    return out
