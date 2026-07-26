"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketMetricsConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.metrics_configuration


class GetBucketMetricsConfigurationOutput(TypedDict, closed=True):
    metrics_configuration: NotRequired[
        "capo_s3.types.metrics_configuration.MetricsConfiguration"
    ]
    """<p>Specifies the metrics configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketMetricsConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "metrics_configuration" in value:
        import capo_s3.types.metrics_configuration

        capo_s3.types.metrics_configuration.serialize_xml(
            value["metrics_configuration"], el, "MetricsConfiguration"
        )


def deserialize_xml(el: Element) -> GetBucketMetricsConfigurationOutput:
    out: GetBucketMetricsConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_metrics_configuration = el.find("MetricsConfiguration")
    if child_metrics_configuration is not None:
        import capo_s3.types.metrics_configuration

        out["metrics_configuration"] = (
            capo_s3.types.metrics_configuration.deserialize_xml(
                child_metrics_configuration
            )
        )
    return out
