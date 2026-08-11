"""Generated from Smithy shape ``com.amazonaws.rds#AvailableAdditionalStorageVolumesOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.available_additional_storage_volumes_option

AvailableAdditionalStorageVolumesOptionList: TypeAlias = list[
    "capo_rds.types.available_additional_storage_volumes_option.AvailableAdditionalStorageVolumesOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableAdditionalStorageVolumesOptionList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.available_additional_storage_volumes_option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.available_additional_storage_volumes_option.serialize_query(
            item, pairs, f"{prefix}.AvailableAdditionalStorageVolumesOption.{n}"
        )


def deserialize_query(el: Element) -> AvailableAdditionalStorageVolumesOptionList:
    import capo_rds.types.available_additional_storage_volumes_option

    out: AvailableAdditionalStorageVolumesOptionList = []
    for child in el.findall("AvailableAdditionalStorageVolumesOption"):
        out.append(
            capo_rds.types.available_additional_storage_volumes_option.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AvailableAdditionalStorageVolumesOptionList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.available_additional_storage_volumes_option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.available_additional_storage_volumes_option.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> AvailableAdditionalStorageVolumesOptionList:
    import capo_rds.types.available_additional_storage_volumes_option

    out: AvailableAdditionalStorageVolumesOptionList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.available_additional_storage_volumes_option.deserialize_query(
                child
            )
        )
    return out
