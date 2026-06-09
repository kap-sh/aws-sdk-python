"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketIntelligentTieringConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.intelligent_tiering_configuration


class GetBucketIntelligentTieringConfigurationOutput(TypedDict):
    intelligent_tiering_configuration: NotRequired[
        "aws_sdk_s3.types.intelligent_tiering_configuration.IntelligentTieringConfiguration"
    ]
    """<p>Container for S3 Intelligent-Tiering configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketIntelligentTieringConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "intelligent_tiering_configuration" in value:
        import aws_sdk_s3.types.intelligent_tiering_configuration

        aws_sdk_s3.types.intelligent_tiering_configuration.serialize_xml(
            value["intelligent_tiering_configuration"],
            el,
            "IntelligentTieringConfiguration",
        )


def deserialize_xml(el: Element) -> GetBucketIntelligentTieringConfigurationOutput:
    out: GetBucketIntelligentTieringConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_intelligent_tiering_configuration = el.find("IntelligentTieringConfiguration")
    if child_intelligent_tiering_configuration is not None:
        import aws_sdk_s3.types.intelligent_tiering_configuration

        out["intelligent_tiering_configuration"] = (
            aws_sdk_s3.types.intelligent_tiering_configuration.deserialize_xml(
                child_intelligent_tiering_configuration
            )
        )
    return out
