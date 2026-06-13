"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListAuditFindingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.audit_findings
    import aws_sdk_application_signals.types.next_token


class ListAuditFindingsOutput(TypedDict):
    start_time: NotRequired["datetime.datetime"]
    """<p>The start of the time period that the returned audit findings apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end of the time period that the returned audit findings apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>"""
    audit_findings: "aws_sdk_application_signals.types.audit_findings.AuditFindings"
    """<p>An array of structures, where each structure contains information about one audit finding, including the auditor results, severity, and associated metric and dependency graphs.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of audit findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditFindingsOutput) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["StartTime"] = (
            aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["EndTime"] = (
            aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    import aws_sdk_application_signals.types.audit_findings

    out["AuditFindings"] = (
        aws_sdk_application_signals.types.audit_findings.serialize_json(
            value["audit_findings"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditFindingsOutput:
    out: ListAuditFindingsOutput = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    if "AuditFindings" in data:
        import aws_sdk_application_signals.types.audit_findings

        out["audit_findings"] = (
            aws_sdk_application_signals.types.audit_findings.deserialize_json(
                data["AuditFindings"]
            )
        )
    else:
        raise DeserializationError("ListAuditFindingsOutput.audit_findings required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
