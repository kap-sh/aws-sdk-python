"""Generated from Smithy shape ``com.amazonaws.rds#ValidAdditionalStorageOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.valid_volume_options_list


class ValidAdditionalStorageOptions(TypedDict, closed=True):
    supports_additional_storage_volumes: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance supports additional storage volumes.</p>"""
    volumes: NotRequired[
        "capo_rds.types.valid_volume_options_list.ValidVolumeOptionsList"
    ]
    """<p>The valid additional storage volume options for the DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidAdditionalStorageOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "supports_additional_storage_volumes" in value:
        pairs.append(
            (
                f"{prefix}.SupportsAdditionalStorageVolumes",
                "true" if value["supports_additional_storage_volumes"] else "false",
            )
        )
    if "volumes" in value:
        import capo_rds.types.valid_volume_options_list

        capo_rds.types.valid_volume_options_list.serialize_query(
            value["volumes"], pairs, f"{prefix}.Volumes"
        )


def deserialize_query(el: Element) -> ValidAdditionalStorageOptions:
    out: ValidAdditionalStorageOptions = {}  # type: ignore[typeddict-item]
    child_supports_additional_storage_volumes = el.find(
        "SupportsAdditionalStorageVolumes"
    )
    if child_supports_additional_storage_volumes is not None:
        out["supports_additional_storage_volumes"] = (
            child_supports_additional_storage_volumes.text or ""
        ).lower() == "true"
    child_volumes = el.find("Volumes")
    if child_volumes is not None:
        import capo_rds.types.valid_volume_options_list

        out["volumes"] = capo_rds.types.valid_volume_options_list.deserialize_query(
            child_volumes
        )
    return out
