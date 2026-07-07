"""Generated from Smithy shape ``com.amazonaws.securityhub#PatchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class PatchSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the compliance standard that was used to determine the patch compliance status.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 256.</p>"""
    installed_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of patches from the compliance standard that were installed successfully.</p> <p>The value can be an integer from <code>0</code> to <code>100000</code>.</p>"""
    missing_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of patches that are part of the compliance standard but are not installed. The count includes patches that failed to install.</p> <p>The value can be an integer from <code>0</code> to <code>100000</code>.</p>"""
    failed_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of patches from the compliance standard that failed to install.</p> <p>The value can be an integer from <code>0</code> to <code>100000</code>.</p>"""
    installed_other_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of installed patches that are not part of the compliance standard.</p> <p>The value can be an integer from <code>0</code> to <code>100000</code>.</p>"""
    installed_rejected_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of patches that are installed but are also on a list of patches that the customer rejected.</p> <p>The value can be an integer from <code>0</code> to <code>100000</code>.</p>"""
    installed_pending_reboot: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of patches that were applied, but that require the instance to be rebooted in order to be marked as installed.</p> <p>The value can be an integer from <code>0</code> to <code>100000</code>.</p>"""
    operation_start_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the operation started.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    operation_end_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the operation completed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    reboot_option: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reboot option specified for the instance.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 256.</p>"""
    operation: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of patch operation performed. For Patch Manager, the values are <code>SCAN</code> and <code>INSTALL</code>.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 256.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatchSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "installed_count" in value:
        out["InstalledCount"] = value["installed_count"]
    if "missing_count" in value:
        out["MissingCount"] = value["missing_count"]
    if "failed_count" in value:
        out["FailedCount"] = value["failed_count"]
    if "installed_other_count" in value:
        out["InstalledOtherCount"] = value["installed_other_count"]
    if "installed_rejected_count" in value:
        out["InstalledRejectedCount"] = value["installed_rejected_count"]
    if "installed_pending_reboot" in value:
        out["InstalledPendingReboot"] = value["installed_pending_reboot"]
    if "operation_start_time" in value:
        out["OperationStartTime"] = value["operation_start_time"]
    if "operation_end_time" in value:
        out["OperationEndTime"] = value["operation_end_time"]
    if "reboot_option" in value:
        out["RebootOption"] = value["reboot_option"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> PatchSummary:
    out: PatchSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "InstalledCount" in data:
        out["installed_count"] = data["InstalledCount"]
    if "MissingCount" in data:
        out["missing_count"] = data["MissingCount"]
    if "FailedCount" in data:
        out["failed_count"] = data["FailedCount"]
    if "InstalledOtherCount" in data:
        out["installed_other_count"] = data["InstalledOtherCount"]
    if "InstalledRejectedCount" in data:
        out["installed_rejected_count"] = data["InstalledRejectedCount"]
    if "InstalledPendingReboot" in data:
        out["installed_pending_reboot"] = data["InstalledPendingReboot"]
    if "OperationStartTime" in data:
        out["operation_start_time"] = data["OperationStartTime"]
    if "OperationEndTime" in data:
        out["operation_end_time"] = data["OperationEndTime"]
    if "RebootOption" in data:
        out["reboot_option"] = data["RebootOption"]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    return out
