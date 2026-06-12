"""Generated from Smithy shape ``com.amazonaws.s3control#BucketLevel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.activity_metrics
    import aws_sdk_s3_control.types.advanced_cost_optimization_metrics
    import aws_sdk_s3_control.types.advanced_data_protection_metrics
    import aws_sdk_s3_control.types.advanced_performance_metrics
    import aws_sdk_s3_control.types.detailed_status_codes_metrics
    import aws_sdk_s3_control.types.prefix_level


class BucketLevel(TypedDict):
    activity_metrics: NotRequired[
        "aws_sdk_s3_control.types.activity_metrics.ActivityMetrics"
    ]
    """<p>A container for the bucket-level activity metrics for S3 Storage Lens.</p>"""
    prefix_level: NotRequired["aws_sdk_s3_control.types.prefix_level.PrefixLevel"]
    """<p>A container for the prefix-level metrics for S3 Storage Lens. </p>"""
    advanced_cost_optimization_metrics: NotRequired[
        "aws_sdk_s3_control.types.advanced_cost_optimization_metrics.AdvancedCostOptimizationMetrics"
    ]
    """<p>A container for bucket-level advanced cost-optimization metrics for S3 Storage Lens.</p>"""
    advanced_data_protection_metrics: NotRequired[
        "aws_sdk_s3_control.types.advanced_data_protection_metrics.AdvancedDataProtectionMetrics"
    ]
    """<p>A container for bucket-level advanced data-protection metrics for S3 Storage Lens.</p>"""
    detailed_status_codes_metrics: NotRequired[
        "aws_sdk_s3_control.types.detailed_status_codes_metrics.DetailedStatusCodesMetrics"
    ]
    """<p>A container for bucket-level detailed status code metrics for S3 Storage Lens.</p>"""
    advanced_performance_metrics: NotRequired[
        "aws_sdk_s3_control.types.advanced_performance_metrics.AdvancedPerformanceMetrics"
    ]
    """<p>A container for bucket-level advanced performance metrics for S3 Storage Lens.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: BucketLevel, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "activity_metrics" in value:
        import aws_sdk_s3_control.types.activity_metrics

        aws_sdk_s3_control.types.activity_metrics.serialize_xml(
            value["activity_metrics"], el, "ActivityMetrics"
        )
    if "prefix_level" in value:
        import aws_sdk_s3_control.types.prefix_level

        aws_sdk_s3_control.types.prefix_level.serialize_xml(
            value["prefix_level"], el, "PrefixLevel"
        )
    if "advanced_cost_optimization_metrics" in value:
        import aws_sdk_s3_control.types.advanced_cost_optimization_metrics

        aws_sdk_s3_control.types.advanced_cost_optimization_metrics.serialize_xml(
            value["advanced_cost_optimization_metrics"],
            el,
            "AdvancedCostOptimizationMetrics",
        )
    if "advanced_data_protection_metrics" in value:
        import aws_sdk_s3_control.types.advanced_data_protection_metrics

        aws_sdk_s3_control.types.advanced_data_protection_metrics.serialize_xml(
            value["advanced_data_protection_metrics"],
            el,
            "AdvancedDataProtectionMetrics",
        )
    if "detailed_status_codes_metrics" in value:
        import aws_sdk_s3_control.types.detailed_status_codes_metrics

        aws_sdk_s3_control.types.detailed_status_codes_metrics.serialize_xml(
            value["detailed_status_codes_metrics"], el, "DetailedStatusCodesMetrics"
        )
    if "advanced_performance_metrics" in value:
        import aws_sdk_s3_control.types.advanced_performance_metrics

        aws_sdk_s3_control.types.advanced_performance_metrics.serialize_xml(
            value["advanced_performance_metrics"], el, "AdvancedPerformanceMetrics"
        )


def deserialize_xml(el: Element) -> BucketLevel:
    out: BucketLevel = {}  # type: ignore[typeddict-item]
    child_activity_metrics = el.find("ActivityMetrics")
    if child_activity_metrics is not None:
        import aws_sdk_s3_control.types.activity_metrics

        out["activity_metrics"] = (
            aws_sdk_s3_control.types.activity_metrics.deserialize_xml(
                child_activity_metrics
            )
        )
    child_prefix_level = el.find("PrefixLevel")
    if child_prefix_level is not None:
        import aws_sdk_s3_control.types.prefix_level

        out["prefix_level"] = aws_sdk_s3_control.types.prefix_level.deserialize_xml(
            child_prefix_level
        )
    child_advanced_cost_optimization_metrics = el.find(
        "AdvancedCostOptimizationMetrics"
    )
    if child_advanced_cost_optimization_metrics is not None:
        import aws_sdk_s3_control.types.advanced_cost_optimization_metrics

        out["advanced_cost_optimization_metrics"] = (
            aws_sdk_s3_control.types.advanced_cost_optimization_metrics.deserialize_xml(
                child_advanced_cost_optimization_metrics
            )
        )
    child_advanced_data_protection_metrics = el.find("AdvancedDataProtectionMetrics")
    if child_advanced_data_protection_metrics is not None:
        import aws_sdk_s3_control.types.advanced_data_protection_metrics

        out["advanced_data_protection_metrics"] = (
            aws_sdk_s3_control.types.advanced_data_protection_metrics.deserialize_xml(
                child_advanced_data_protection_metrics
            )
        )
    child_detailed_status_codes_metrics = el.find("DetailedStatusCodesMetrics")
    if child_detailed_status_codes_metrics is not None:
        import aws_sdk_s3_control.types.detailed_status_codes_metrics

        out["detailed_status_codes_metrics"] = (
            aws_sdk_s3_control.types.detailed_status_codes_metrics.deserialize_xml(
                child_detailed_status_codes_metrics
            )
        )
    child_advanced_performance_metrics = el.find("AdvancedPerformanceMetrics")
    if child_advanced_performance_metrics is not None:
        import aws_sdk_s3_control.types.advanced_performance_metrics

        out["advanced_performance_metrics"] = (
            aws_sdk_s3_control.types.advanced_performance_metrics.deserialize_xml(
                child_advanced_performance_metrics
            )
        )
    return out
