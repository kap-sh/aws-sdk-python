"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupOptionVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_version

OptionGroupOptionVersionsList: TypeAlias = list[
    "capo_rds.types.option_version.OptionVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupOptionVersionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_version

    for n, item in enumerate(value, 1):
        capo_rds.types.option_version.serialize_query(
            item, pairs, f"{prefix}.OptionVersion.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupOptionVersionsList:
    import capo_rds.types.option_version

    out: OptionGroupOptionVersionsList = []
    for child in el.findall("OptionVersion"):
        out.append(capo_rds.types.option_version.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionGroupOptionVersionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_version

    for n, item in enumerate(value, 1):
        capo_rds.types.option_version.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupOptionVersionsList:
    import capo_rds.types.option_version

    out: OptionGroupOptionVersionsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.option_version.deserialize_query(child))
    return out
