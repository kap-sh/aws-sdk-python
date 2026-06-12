"""Generated from Smithy shape ``com.amazonaws.s3control#AccountLevel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.activity_metrics
    import aws_sdk_s3_control.types.advanced_cost_optimization_metrics
    import aws_sdk_s3_control.types.advanced_data_protection_metrics
    import aws_sdk_s3_control.types.advanced_performance_metrics
    import aws_sdk_s3_control.types.bucket_level
    import aws_sdk_s3_control.types.detailed_status_codes_metrics
    import aws_sdk_s3_control.types.storage_lens_group_level


class AccountLevel(TypedDict):
    activity_metrics: NotRequired[
        "aws_sdk_s3_control.types.activity_metrics.ActivityMetrics"
    ]
    """<p>A container element for S3 Storage Lens activity metrics.</p>"""
    bucket_level: "aws_sdk_s3_control.types.bucket_level.BucketLevel"
    """<p>A container element for the S3 Storage Lens bucket-level configuration.</p>"""
    advanced_cost_optimization_metrics: NotRequired[
        "aws_sdk_s3_control.types.advanced_cost_optimization_metrics.AdvancedCostOptimizationMetrics"
    ]
    """<p>A container element for S3 Storage Lens advanced cost-optimization metrics.</p>"""
    advanced_data_protection_metrics: NotRequired[
        "aws_sdk_s3_control.types.advanced_data_protection_metrics.AdvancedDataProtectionMetrics"
    ]
    """<p>A container element for S3 Storage Lens advanced data-protection metrics.</p>"""
    detailed_status_codes_metrics: NotRequired[
        "aws_sdk_s3_control.types.detailed_status_codes_metrics.DetailedStatusCodesMetrics"
    ]
    """<p>A container element for detailed status code metrics. </p>"""
    advanced_performance_metrics: NotRequired[
        "aws_sdk_s3_control.types.advanced_performance_metrics.AdvancedPerformanceMetrics"
    ]
    """<p>A container element for S3 Storage Lens advanced performance metrics.</p>"""
    storage_lens_group_level: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_group_level.StorageLensGroupLevel"
    ]
    """<p> A container element for S3 Storage Lens groups metrics. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: AccountLevel, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "activity_metrics" in value:
        import aws_sdk_s3_control.types.activity_metrics

        aws_sdk_s3_control.types.activity_metrics.serialize_xml(
            value["activity_metrics"], el, "ActivityMetrics"
        )
    import aws_sdk_s3_control.types.bucket_level

    aws_sdk_s3_control.types.bucket_level.serialize_xml(
        value["bucket_level"], el, "BucketLevel"
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
    if "storage_lens_group_level" in value:
        import aws_sdk_s3_control.types.storage_lens_group_level

        aws_sdk_s3_control.types.storage_lens_group_level.serialize_xml(
            value["storage_lens_group_level"], el, "StorageLensGroupLevel"
        )


def deserialize_xml(el: Element) -> AccountLevel:
    out: AccountLevel = {}  # type: ignore[typeddict-item]
    child_activity_metrics = el.find("ActivityMetrics")
    if child_activity_metrics is not None:
        import aws_sdk_s3_control.types.activity_metrics

        out["activity_metrics"] = (
            aws_sdk_s3_control.types.activity_metrics.deserialize_xml(
                child_activity_metrics
            )
        )
    child_bucket_level = el.find("BucketLevel")
    if child_bucket_level is not None:
        import aws_sdk_s3_control.types.bucket_level

        out["bucket_level"] = aws_sdk_s3_control.types.bucket_level.deserialize_xml(
            child_bucket_level
        )
    else:
        raise DeserializationError("AccountLevel.bucket_level required")
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
    child_storage_lens_group_level = el.find("StorageLensGroupLevel")
    if child_storage_lens_group_level is not None:
        import aws_sdk_s3_control.types.storage_lens_group_level

        out["storage_lens_group_level"] = (
            aws_sdk_s3_control.types.storage_lens_group_level.deserialize_xml(
                child_storage_lens_group_level
            )
        )
    return out
