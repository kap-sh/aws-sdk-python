"""Generated from Smithy shape ``com.amazonaws.ec2#GetDeclarativePoliciesReportSummaryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_summary_list
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class GetDeclarativePoliciesReportSummaryResult(TypedDict, closed=True):
    report_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the report.</p>"""
    s3_bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket where the report is located.</p>"""
    s3_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The prefix for your S3 object.</p>"""
    target_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The root ID, organizational unit ID, or account ID.</p> <p>Format:</p> <ul> <li> <p>For root: <code>r-ab12</code> </p> </li> <li> <p>For OU: <code>ou-ab12-cdef1234</code> </p> </li> <li> <p>For account: <code>123456789012</code> </p> </li> </ul>"""
    start_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time when the report generation started.</p>"""
    end_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The time when the report generation ended.</p>"""
    number_of_accounts: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of accounts associated with the specified <code>targetId</code>.</p>"""
    number_of_failed_accounts: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of accounts where attributes could not be retrieved in any Region.</p>"""
    attribute_summaries: NotRequired[
        "capo_ec2.types.attribute_summary_list.AttributeSummaryList"
    ]
    """<p>The attributes described in the report.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetDeclarativePoliciesReportSummaryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "report_id" in value:
        pairs.append((f"{key_prefix}ReportId", str(value["report_id"])))
    if "s3_bucket" in value:
        pairs.append((f"{key_prefix}S3Bucket", str(value["s3_bucket"])))
    if "s3_prefix" in value:
        pairs.append((f"{key_prefix}S3Prefix", str(value["s3_prefix"])))
    if "target_id" in value:
        pairs.append((f"{key_prefix}TargetId", str(value["target_id"])))
    if "start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "number_of_accounts" in value:
        pairs.append(
            (f"{key_prefix}NumberOfAccounts", str(value["number_of_accounts"]))
        )
    if "number_of_failed_accounts" in value:
        pairs.append(
            (
                f"{key_prefix}NumberOfFailedAccounts",
                str(value["number_of_failed_accounts"]),
            )
        )
    if "attribute_summaries" in value:
        import capo_ec2.types.attribute_summary_list

        capo_ec2.types.attribute_summary_list.serialize_ec2_query(
            value["attribute_summaries"], pairs, f"{key_prefix}AttributeSummarySet"
        )


def deserialize_ec2_query(el: Element) -> GetDeclarativePoliciesReportSummaryResult:
    out: GetDeclarativePoliciesReportSummaryResult = {}  # type: ignore[typeddict-item]
    child_report_id = el.find("ReportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_prefix = el.find("S3Prefix")
    if child_s3_prefix is not None:
        out["s3_prefix"] = str(child_s3_prefix.text or "")
    child_target_id = el.find("TargetId")
    if child_target_id is not None:
        out["target_id"] = str(child_target_id.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_time
        )
    child_number_of_accounts = el.find("NumberOfAccounts")
    if child_number_of_accounts is not None:
        out["number_of_accounts"] = int(child_number_of_accounts.text or "")
    child_number_of_failed_accounts = el.find("NumberOfFailedAccounts")
    if child_number_of_failed_accounts is not None:
        out["number_of_failed_accounts"] = int(
            child_number_of_failed_accounts.text or ""
        )
    if el.find("AttributeSummarySet") is not None:
        import capo_ec2.types.attribute_summary_list

        out["attribute_summaries"] = (
            capo_ec2.types.attribute_summary_list.deserialize_ec2_query(
                el, "AttributeSummarySet"
            )
        )
    return out
