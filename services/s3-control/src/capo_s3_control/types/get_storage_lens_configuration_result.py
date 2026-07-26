"""Generated from Smithy shape ``com.amazonaws.s3control#GetStorageLensConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_configuration


class GetStorageLensConfigurationResult(TypedDict, closed=True):
    storage_lens_configuration: NotRequired[
        "capo_s3_control.types.storage_lens_configuration.StorageLensConfiguration"
    ]
    """<p>The S3 Storage Lens configuration requested.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetStorageLensConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "storage_lens_configuration" in value:
        import capo_s3_control.types.storage_lens_configuration

        capo_s3_control.types.storage_lens_configuration.serialize_xml(
            value["storage_lens_configuration"], el, "StorageLensConfiguration"
        )


def deserialize_xml(el: Element) -> GetStorageLensConfigurationResult:
    out: GetStorageLensConfigurationResult = {}  # type: ignore[typeddict-item]
    child_storage_lens_configuration = el.find("StorageLensConfiguration")
    if child_storage_lens_configuration is not None:
        import capo_s3_control.types.storage_lens_configuration

        out["storage_lens_configuration"] = (
            capo_s3_control.types.storage_lens_configuration.deserialize_xml(
                child_storage_lens_configuration
            )
        )
    return out
