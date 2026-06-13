"""Generated from Smithy shape ``com.amazonaws.inspector2#StopCisMessageProgress``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.check_count


class StopCisMessageProgress(TypedDict):
    total_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' total checks.</p>"""
    successful_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' successful checks.</p>"""
    failed_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' failed checks.</p>"""
    not_evaluated_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' not evaluated checks.</p>"""
    unknown_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' unknown checks.</p>"""
    not_applicable_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' not applicable checks.</p>"""
    informational_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' informational checks.</p>"""
    error_checks: "aws_sdk_inspector2.types.check_count.CheckCount"
    """<p>The progress' error checks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCisMessageProgress) -> dict:
    out: dict = {}
    out["totalChecks"] = value.get("total_checks", 0)
    out["successfulChecks"] = value.get("successful_checks", 0)
    out["failedChecks"] = value.get("failed_checks", 0)
    out["notEvaluatedChecks"] = value.get("not_evaluated_checks", 0)
    out["unknownChecks"] = value.get("unknown_checks", 0)
    out["notApplicableChecks"] = value.get("not_applicable_checks", 0)
    out["informationalChecks"] = value.get("informational_checks", 0)
    out["errorChecks"] = value.get("error_checks", 0)
    return out


def deserialize_json(data: dict) -> StopCisMessageProgress:
    out: StopCisMessageProgress = {}  # type: ignore[typeddict-item]
    if "totalChecks" in data:
        out["total_checks"] = data["totalChecks"]
    else:
        out["total_checks"] = 0
    if "successfulChecks" in data:
        out["successful_checks"] = data["successfulChecks"]
    else:
        out["successful_checks"] = 0
    if "failedChecks" in data:
        out["failed_checks"] = data["failedChecks"]
    else:
        out["failed_checks"] = 0
    if "notEvaluatedChecks" in data:
        out["not_evaluated_checks"] = data["notEvaluatedChecks"]
    else:
        out["not_evaluated_checks"] = 0
    if "unknownChecks" in data:
        out["unknown_checks"] = data["unknownChecks"]
    else:
        out["unknown_checks"] = 0
    if "notApplicableChecks" in data:
        out["not_applicable_checks"] = data["notApplicableChecks"]
    else:
        out["not_applicable_checks"] = 0
    if "informationalChecks" in data:
        out["informational_checks"] = data["informationalChecks"]
    else:
        out["informational_checks"] = 0
    if "errorChecks" in data:
        out["error_checks"] = data["errorChecks"]
    else:
        out["error_checks"] = 0
    return out
