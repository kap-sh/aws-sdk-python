"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensTableDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.is_enabled
    import capo_s3_control.types.storage_lens_data_export_encryption


class StorageLensTableDestination(TypedDict, closed=True):
    is_enabled: "capo_s3_control.types.is_enabled.IsEnabled"
    """<p>A container that indicates whether the export to read-only S3 table buckets is enabled for your S3 Storage Lens configuration. When set to true, Storage Lens reports are automatically exported to tables in addition to other configured destinations.</p>"""
    encryption: NotRequired[
        "capo_s3_control.types.storage_lens_data_export_encryption.StorageLensDataExportEncryption"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensTableDestination, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "IsEnabled").text = (
        "true" if value.get("is_enabled", False) else "false"
    )
    if "encryption" in value:
        import capo_s3_control.types.storage_lens_data_export_encryption

        capo_s3_control.types.storage_lens_data_export_encryption.serialize_xml(
            value["encryption"], el, "Encryption"
        )


def deserialize_xml(el: Element) -> StorageLensTableDestination:
    out: StorageLensTableDestination = {}  # type: ignore[typeddict-item]
    child_is_enabled = el.find("IsEnabled")
    if child_is_enabled is not None:
        out["is_enabled"] = (child_is_enabled.text or "").lower() == "true"
    else:
        out["is_enabled"] = False
    child_encryption = el.find("Encryption")
    if child_encryption is not None:
        import capo_s3_control.types.storage_lens_data_export_encryption

        out["encryption"] = (
            capo_s3_control.types.storage_lens_data_export_encryption.deserialize_xml(
                child_encryption
            )
        )
    return out
