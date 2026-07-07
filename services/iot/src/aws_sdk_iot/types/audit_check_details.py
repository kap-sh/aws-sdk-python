"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_run_status
    import aws_sdk_iot.types.check_compliant
    import aws_sdk_iot.types.error_code
    import aws_sdk_iot.types.error_message
    import aws_sdk_iot.types.non_compliant_resources_count
    import aws_sdk_iot.types.suppressed_non_compliant_resources_count
    import aws_sdk_iot.types.total_resources_count


class AuditCheckDetails(TypedDict, closed=True):
    check_run_status: NotRequired[
        "aws_sdk_iot.types.audit_check_run_status.AuditCheckRunStatus"
    ]
    r"""<p>The completion status of this check. One of \"IN_PROGRESS\", \"WAITING_FOR_DATA_COLLECTION\", \"CANCELED\", \"COMPLETED_COMPLIANT\", \"COMPLETED_NON_COMPLIANT\", or \"FAILED\".</p>"""
    check_compliant: NotRequired["aws_sdk_iot.types.check_compliant.CheckCompliant"]
    """<p>True if the check is complete and found all resources compliant.</p>"""
    total_resources_count: NotRequired[
        "aws_sdk_iot.types.total_resources_count.TotalResourcesCount"
    ]
    """<p>The number of resources on which the check was performed.</p>"""
    non_compliant_resources_count: NotRequired[
        "aws_sdk_iot.types.non_compliant_resources_count.NonCompliantResourcesCount"
    ]
    """<p>The number of resources that were found noncompliant during the check.</p>"""
    suppressed_non_compliant_resources_count: NotRequired[
        "aws_sdk_iot.types.suppressed_non_compliant_resources_count.SuppressedNonCompliantResourcesCount"
    ]
    """<p> Describes how many of the non-compliant resources created during the evaluation of an audit check were marked as suppressed. </p>"""
    error_code: NotRequired["aws_sdk_iot.types.error_code.ErrorCode"]
    r"""<p>The code of any error encountered when this check is performed during this audit. One of \"INSUFFICIENT_PERMISSIONS\" or \"AUDIT_CHECK_DISABLED\".</p>"""
    message: NotRequired["aws_sdk_iot.types.error_message.ErrorMessage"]
    """<p>The message associated with any error encountered when this check is performed during this audit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditCheckDetails) -> dict:
    out: dict = {}
    if "check_run_status" in value:
        import aws_sdk_iot.types.audit_check_run_status

        out["checkRunStatus"] = aws_sdk_iot.types.audit_check_run_status.serialize_json(
            value["check_run_status"]
        )
    if "check_compliant" in value:
        out["checkCompliant"] = value["check_compliant"]
    if "total_resources_count" in value:
        out["totalResourcesCount"] = value["total_resources_count"]
    if "non_compliant_resources_count" in value:
        out["nonCompliantResourcesCount"] = value["non_compliant_resources_count"]
    if "suppressed_non_compliant_resources_count" in value:
        out["suppressedNonCompliantResourcesCount"] = value[
            "suppressed_non_compliant_resources_count"
        ]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AuditCheckDetails:
    out: AuditCheckDetails = {}  # type: ignore[typeddict-item]
    if "checkRunStatus" in data:
        import aws_sdk_iot.types.audit_check_run_status

        out["check_run_status"] = (
            aws_sdk_iot.types.audit_check_run_status.deserialize_json(
                data["checkRunStatus"]
            )
        )
    if "checkCompliant" in data:
        out["check_compliant"] = data["checkCompliant"]
    if "totalResourcesCount" in data:
        out["total_resources_count"] = data["totalResourcesCount"]
    if "nonCompliantResourcesCount" in data:
        out["non_compliant_resources_count"] = data["nonCompliantResourcesCount"]
    if "suppressedNonCompliantResourcesCount" in data:
        out["suppressed_non_compliant_resources_count"] = data[
            "suppressedNonCompliantResourcesCount"
        ]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "message" in data:
        out["message"] = data["message"]
    return out
