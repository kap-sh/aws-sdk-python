"""Generated from Smithy shape ``com.amazonaws.s3control#JobReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.boolean
    import capo_s3_control.types.job_report_format
    import capo_s3_control.types.job_report_scope
    import capo_s3_control.types.report_prefix_string
    import capo_s3_control.types.s3_bucket_arn_string


class JobReport(TypedDict, closed=True):
    bucket: NotRequired["capo_s3_control.types.s3_bucket_arn_string.S3BucketArnString"]
    """<p>The Amazon Resource Name (ARN) for the bucket where specified job-completion report will be stored.</p> <note> <p> <b>Directory buckets</b> - Directory buckets aren't supported as a location for Batch Operations to store job completion reports.</p> </note>"""
    format: NotRequired["capo_s3_control.types.job_report_format.JobReportFormat"]
    """<p>The format of the specified job-completion report.</p>"""
    enabled: "capo_s3_control.types.boolean.Boolean"
    """<p>Indicates whether the specified job will generate a job-completion report.</p>"""
    prefix: NotRequired["capo_s3_control.types.report_prefix_string.ReportPrefixString"]
    """<p>An optional prefix to describe where in the specified bucket the job-completion report will be stored. Amazon S3 stores the job-completion report at <code><prefix>/job-<job-id>/report.json</code>.</p>"""
    report_scope: NotRequired["capo_s3_control.types.job_report_scope.JobReportScope"]
    """<p>Indicates whether the job-completion report will include details of all tasks or only failed tasks.</p>"""
    expected_bucket_owner: NotRequired["capo_s3_control.types.account_id.AccountId"]
    """<p>Lists the Amazon Web Services account ID that owns the target bucket, where the completion report is received.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobReport, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "format" in value:
        import capo_s3_control.types.job_report_format

        capo_s3_control.types.job_report_format.serialize_xml(
            value["format"], el, "Format"
        )
    SubElement(el, "Enabled").text = "true" if value.get("enabled", False) else "false"
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "report_scope" in value:
        import capo_s3_control.types.job_report_scope

        capo_s3_control.types.job_report_scope.serialize_xml(
            value["report_scope"], el, "ReportScope"
        )
    if "expected_bucket_owner" in value:
        SubElement(el, "ExpectedBucketOwner").text = str(value["expected_bucket_owner"])


def deserialize_xml(el: Element) -> JobReport:
    out: JobReport = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_format = el.find("Format")
    if child_format is not None:
        import capo_s3_control.types.job_report_format

        out["format"] = capo_s3_control.types.job_report_format.deserialize_xml(
            child_format
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_report_scope = el.find("ReportScope")
    if child_report_scope is not None:
        import capo_s3_control.types.job_report_scope

        out["report_scope"] = capo_s3_control.types.job_report_scope.deserialize_xml(
            child_report_scope
        )
    child_expected_bucket_owner = el.find("ExpectedBucketOwner")
    if child_expected_bucket_owner is not None:
        out["expected_bucket_owner"] = str(child_expected_bucket_owner.text or "")
    return out
