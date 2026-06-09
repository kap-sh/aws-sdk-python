"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketMetricsConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.metrics_configuration


class GetBucketMetricsConfigurationOutput(TypedDict):
    metrics_configuration: NotRequired[
        "aws_sdk_s3.types.metrics_configuration.MetricsConfiguration"
    ]
    """<p>Specifies the metrics configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketMetricsConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "metrics_configuration" in value:
        import aws_sdk_s3.types.metrics_configuration

        aws_sdk_s3.types.metrics_configuration.serialize_xml(
            value["metrics_configuration"], el, "MetricsConfiguration"
        )


def deserialize_xml(el: Element) -> GetBucketMetricsConfigurationOutput:
    out: GetBucketMetricsConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_metrics_configuration = el.find("MetricsConfiguration")
    if child_metrics_configuration is not None:
        import aws_sdk_s3.types.metrics_configuration

        out["metrics_configuration"] = (
            aws_sdk_s3.types.metrics_configuration.deserialize_xml(
                child_metrics_configuration
            )
        )
    return out
