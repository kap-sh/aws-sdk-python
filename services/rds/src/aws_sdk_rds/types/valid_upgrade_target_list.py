"""Generated from Smithy shape ``com.amazonaws.rds#ValidUpgradeTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.upgrade_target

ValidUpgradeTargetList: TypeAlias = list[
    "aws_sdk_rds.types.upgrade_target.UpgradeTarget"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidUpgradeTargetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.upgrade_target

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.upgrade_target.serialize_query(
            item, pairs, f"{prefix}.UpgradeTarget.{n}"
        )


def deserialize_query(el: Element) -> ValidUpgradeTargetList:
    import aws_sdk_rds.types.upgrade_target

    out: ValidUpgradeTargetList = []
    for child in el.findall("UpgradeTarget"):
        out.append(aws_sdk_rds.types.upgrade_target.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ValidUpgradeTargetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.upgrade_target

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.upgrade_target.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ValidUpgradeTargetList:
    import aws_sdk_rds.types.upgrade_target

    out: ValidUpgradeTargetList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.upgrade_target.deserialize_query(child))
    return out
