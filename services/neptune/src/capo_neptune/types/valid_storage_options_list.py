"""Generated from Smithy shape ``com.amazonaws.neptune#ValidStorageOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.valid_storage_options

ValidStorageOptionsList: TypeAlias = list[
    "capo_neptune.types.valid_storage_options.ValidStorageOptions"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidStorageOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.valid_storage_options

    for n, item in enumerate(value, 1):
        capo_neptune.types.valid_storage_options.serialize_query(
            item, pairs, f"{prefix}.ValidStorageOptions.{n}"
        )


def deserialize_query(el: Element) -> ValidStorageOptionsList:
    import capo_neptune.types.valid_storage_options

    out: ValidStorageOptionsList = []
    for child in el.findall("ValidStorageOptions"):
        out.append(capo_neptune.types.valid_storage_options.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ValidStorageOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.valid_storage_options

    for n, item in enumerate(value, 1):
        capo_neptune.types.valid_storage_options.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ValidStorageOptionsList:
    import capo_neptune.types.valid_storage_options

    out: ValidStorageOptionsList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.valid_storage_options.deserialize_query(child))
    return out
