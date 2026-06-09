"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketCorsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.cors_rules


class GetBucketCorsOutput(TypedDict):
    cors_rules: NotRequired["aws_sdk_s3.types.cors_rules.CORSRules"]
    """<p>A set of origins and methods (cross-origin access that you want to allow). You can add up to 100 rules to the configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketCorsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "cors_rules" in value:
        import aws_sdk_s3.types.cors_rules

        aws_sdk_s3.types.cors_rules.serialize_xml_flat(
            value["cors_rules"], el, "CORSRule"
        )


def deserialize_xml(el: Element) -> GetBucketCorsOutput:
    out: GetBucketCorsOutput = {}  # type: ignore[typeddict-item]
    if el.find("CORSRule") is not None:
        import aws_sdk_s3.types.cors_rules

        out["cors_rules"] = aws_sdk_s3.types.cors_rules.deserialize_xml_flat(
            el, "CORSRule"
        )
    return out
