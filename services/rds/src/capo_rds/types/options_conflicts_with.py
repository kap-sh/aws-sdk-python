"""Generated from Smithy shape ``com.amazonaws.rds#OptionsConflictsWith``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string

OptionsConflictsWith: TypeAlias = list["capo_rds.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionsConflictsWith, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.OptionConflictName.{n}", str(item)))


def deserialize_query(el: Element) -> OptionsConflictsWith:
    out: OptionsConflictsWith = []
    for child in el.findall("OptionConflictName"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: OptionsConflictsWith, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> OptionsConflictsWith:
    out: OptionsConflictsWith = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
