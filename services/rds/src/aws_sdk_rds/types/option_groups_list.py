"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_group

OptionGroupsList: TypeAlias = list["aws_sdk_rds.types.option_group.OptionGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_group

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_group.serialize_query(
            item, pairs, f"{prefix}.OptionGroup.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupsList:
    import aws_sdk_rds.types.option_group

    out: OptionGroupsList = []
    for child in el.findall("OptionGroup"):
        out.append(aws_sdk_rds.types.option_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionGroupsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_group

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupsList:
    import aws_sdk_rds.types.option_group

    out: OptionGroupsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.option_group.deserialize_query(child))
    return out
