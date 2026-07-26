"""Generated from Smithy shape ``com.amazonaws.neptune#SupportedCharacterSetsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.character_set

SupportedCharacterSetsList: TypeAlias = list[
    "capo_neptune.types.character_set.CharacterSet"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedCharacterSetsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.character_set

    for n, item in enumerate(value, 1):
        capo_neptune.types.character_set.serialize_query(
            item, pairs, f"{prefix}.CharacterSet.{n}"
        )


def deserialize_query(el: Element) -> SupportedCharacterSetsList:
    import capo_neptune.types.character_set

    out: SupportedCharacterSetsList = []
    for child in el.findall("CharacterSet"):
        out.append(capo_neptune.types.character_set.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedCharacterSetsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.character_set

    for n, item in enumerate(value, 1):
        capo_neptune.types.character_set.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SupportedCharacterSetsList:
    import capo_neptune.types.character_set

    out: SupportedCharacterSetsList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.character_set.deserialize_query(child))
    return out
