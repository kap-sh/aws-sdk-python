"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_group_option

OptionGroupOptionsList: TypeAlias = list[
    "capo_rds.types.option_group_option.OptionGroupOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_group_option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_group_option.serialize_query(
            item, pairs, f"{prefix}.OptionGroupOption.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupOptionsList:
    import capo_rds.types.option_group_option

    out: OptionGroupOptionsList = []
    for child in el.findall("OptionGroupOption"):
        out.append(capo_rds.types.option_group_option.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionGroupOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_group_option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_group_option.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupOptionsList:
    import capo_rds.types.option_group_option

    out: OptionGroupOptionsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.option_group_option.deserialize_query(child))
    return out
