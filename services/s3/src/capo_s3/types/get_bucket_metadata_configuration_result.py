"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketMetadataConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.metadata_configuration_result


class GetBucketMetadataConfigurationResult(TypedDict, closed=True):
    metadata_configuration_result: (
        "capo_s3.types.metadata_configuration_result.MetadataConfigurationResult"
    )
    """<p> The metadata configuration for a general purpose bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketMetadataConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.metadata_configuration_result

    capo_s3.types.metadata_configuration_result.serialize_xml(
        value["metadata_configuration_result"], el, "MetadataConfigurationResult"
    )


def deserialize_xml(el: Element) -> GetBucketMetadataConfigurationResult:
    out: GetBucketMetadataConfigurationResult = {}  # type: ignore[typeddict-item]
    child_metadata_configuration_result = el.find("MetadataConfigurationResult")
    if child_metadata_configuration_result is not None:
        import capo_s3.types.metadata_configuration_result

        out["metadata_configuration_result"] = (
            capo_s3.types.metadata_configuration_result.deserialize_xml(
                child_metadata_configuration_result
            )
        )
    else:
        raise DeserializationError(
            "GetBucketMetadataConfigurationResult.metadata_configuration_result required"
        )
    return out
