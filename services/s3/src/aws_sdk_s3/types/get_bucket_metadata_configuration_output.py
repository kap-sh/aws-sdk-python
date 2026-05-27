"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketMetadataConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.get_bucket_metadata_configuration_result


class GetBucketMetadataConfigurationOutput(TypedDict):
    get_bucket_metadata_configuration_result: NotRequired[
        "aws_sdk_s3.types.get_bucket_metadata_configuration_result.GetBucketMetadataConfigurationResult"
    ]
    """<p> The metadata configuration for the general purpose bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketMetadataConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "get_bucket_metadata_configuration_result" in value:
        import aws_sdk_s3.types.get_bucket_metadata_configuration_result

        aws_sdk_s3.types.get_bucket_metadata_configuration_result.serialize_xml(
            value["get_bucket_metadata_configuration_result"],
            el,
            "GetBucketMetadataConfigurationResult",
        )


def deserialize_xml(el: Element) -> GetBucketMetadataConfigurationOutput:
    out: GetBucketMetadataConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_get_bucket_metadata_configuration_result = el.find(
        "GetBucketMetadataConfigurationResult"
    )
    if child_get_bucket_metadata_configuration_result is not None:
        import aws_sdk_s3.types.get_bucket_metadata_configuration_result

        out["get_bucket_metadata_configuration_result"] = (
            aws_sdk_s3.types.get_bucket_metadata_configuration_result.deserialize_xml(
                child_get_bucket_metadata_configuration_result
            )
        )
    return out
