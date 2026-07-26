"""Generated from Smithy shape ``com.amazonaws.rds#ValidDBInstanceModificationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.available_processor_feature_list
    import capo_rds.types.boolean
    import capo_rds.types.valid_additional_storage_options
    import capo_rds.types.valid_storage_options_list


class ValidDBInstanceModificationsMessage(TypedDict, closed=True):
    storage: NotRequired[
        "capo_rds.types.valid_storage_options_list.ValidStorageOptionsList"
    ]
    """<p>Valid storage options for your DB instance.</p>"""
    valid_processor_features: NotRequired[
        "capo_rds.types.available_processor_feature_list.AvailableProcessorFeatureList"
    ]
    """<p>Valid processor features for your DB instance.</p>"""
    supports_dedicated_log_volume: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports using a dedicated log volume (DLV).</p>"""
    additional_storage: NotRequired[
        "capo_rds.types.valid_additional_storage_options.ValidAdditionalStorageOptions"
    ]
    """<p>The valid additional storage options for the DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidDBInstanceModificationsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "storage" in value:
        import capo_rds.types.valid_storage_options_list

        capo_rds.types.valid_storage_options_list.serialize_query(
            value["storage"], pairs, f"{prefix}.Storage"
        )
    if "valid_processor_features" in value:
        import capo_rds.types.available_processor_feature_list

        capo_rds.types.available_processor_feature_list.serialize_query(
            value["valid_processor_features"], pairs, f"{prefix}.ValidProcessorFeatures"
        )
    if "supports_dedicated_log_volume" in value:
        pairs.append(
            (
                f"{prefix}.SupportsDedicatedLogVolume",
                "true" if value["supports_dedicated_log_volume"] else "false",
            )
        )
    if "additional_storage" in value:
        import capo_rds.types.valid_additional_storage_options

        capo_rds.types.valid_additional_storage_options.serialize_query(
            value["additional_storage"], pairs, f"{prefix}.AdditionalStorage"
        )


def deserialize_query(el: Element) -> ValidDBInstanceModificationsMessage:
    out: ValidDBInstanceModificationsMessage = {}  # type: ignore[typeddict-item]
    child_storage = el.find("Storage")
    if child_storage is not None:
        import capo_rds.types.valid_storage_options_list

        out["storage"] = capo_rds.types.valid_storage_options_list.deserialize_query(
            child_storage
        )
    child_valid_processor_features = el.find("ValidProcessorFeatures")
    if child_valid_processor_features is not None:
        import capo_rds.types.available_processor_feature_list

        out["valid_processor_features"] = (
            capo_rds.types.available_processor_feature_list.deserialize_query(
                child_valid_processor_features
            )
        )
    child_supports_dedicated_log_volume = el.find("SupportsDedicatedLogVolume")
    if child_supports_dedicated_log_volume is not None:
        out["supports_dedicated_log_volume"] = (
            child_supports_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_additional_storage = el.find("AdditionalStorage")
    if child_additional_storage is not None:
        import capo_rds.types.valid_additional_storage_options

        out["additional_storage"] = (
            capo_rds.types.valid_additional_storage_options.deserialize_query(
                child_additional_storage
            )
        )
    return out
