"""Generated from Smithy shape ``com.amazonaws.rds#OptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option

OptionsList: TypeAlias = list["aws_sdk_rds.types.option.Option"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option.serialize_query(item, pairs, f"{prefix}.Option.{n}")


def deserialize_query(el: Element) -> OptionsList:
    import aws_sdk_rds.types.option

    out: OptionsList = []
    for child in el.findall("Option"):
        out.append(aws_sdk_rds.types.option.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionsList:
    import aws_sdk_rds.types.option

    out: OptionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.option.deserialize_query(child))
    return out
