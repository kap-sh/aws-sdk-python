"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketAnalyticsConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.analytics_configuration


class GetBucketAnalyticsConfigurationOutput(TypedDict, closed=True):
    analytics_configuration: NotRequired[
        "aws_sdk_s3.types.analytics_configuration.AnalyticsConfiguration"
    ]
    """<p>The configuration and any analyses for the analytics filter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketAnalyticsConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "analytics_configuration" in value:
        import aws_sdk_s3.types.analytics_configuration

        aws_sdk_s3.types.analytics_configuration.serialize_xml(
            value["analytics_configuration"], el, "AnalyticsConfiguration"
        )


def deserialize_xml(el: Element) -> GetBucketAnalyticsConfigurationOutput:
    out: GetBucketAnalyticsConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_analytics_configuration = el.find("AnalyticsConfiguration")
    if child_analytics_configuration is not None:
        import aws_sdk_s3.types.analytics_configuration

        out["analytics_configuration"] = (
            aws_sdk_s3.types.analytics_configuration.deserialize_xml(
                child_analytics_configuration
            )
        )
    return out
