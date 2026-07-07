"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketLifecycleConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.lifecycle_rules


class GetBucketLifecycleConfigurationResult(TypedDict, closed=True):
    rules: NotRequired["aws_sdk_s3_control.types.lifecycle_rules.LifecycleRules"]
    """<p>Container for the lifecycle rule of the Outposts bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketLifecycleConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "rules" in value:
        import aws_sdk_s3_control.types.lifecycle_rules

        aws_sdk_s3_control.types.lifecycle_rules.serialize_xml(
            value["rules"], el, "Rules"
        )


def deserialize_xml(el: Element) -> GetBucketLifecycleConfigurationResult:
    out: GetBucketLifecycleConfigurationResult = {}  # type: ignore[typeddict-item]
    child_rules = el.find("Rules")
    if child_rules is not None:
        import aws_sdk_s3_control.types.lifecycle_rules

        out["rules"] = aws_sdk_s3_control.types.lifecycle_rules.deserialize_xml(
            child_rules
        )
    return out
