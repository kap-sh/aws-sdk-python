"""Generated from Smithy shape ``com.amazonaws.securityhub#ProcessDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class ProcessDetails(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the process.</p> <p>Length Constraints: Minimum of 1. Maximum of 64.</p>"""
    path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the process executable.</p> <p>Length Constraints: Minimum of 1. Maximum of 512.</p>"""
    pid: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The process ID.</p>"""
    parent_pid: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The parent process ID. This field accepts positive integers between <code>O</code> and <code>2147483647</code>.</p>"""
    launched_at: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the process was launched.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    terminated_at: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the process was terminated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "pid" in value:
        out["Pid"] = value["pid"]
    if "parent_pid" in value:
        out["ParentPid"] = value["parent_pid"]
    if "launched_at" in value:
        out["LaunchedAt"] = value["launched_at"]
    if "terminated_at" in value:
        out["TerminatedAt"] = value["terminated_at"]
    return out


def deserialize_json(data: dict) -> ProcessDetails:
    out: ProcessDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Pid" in data:
        out["pid"] = data["Pid"]
    if "ParentPid" in data:
        out["parent_pid"] = data["ParentPid"]
    if "LaunchedAt" in data:
        out["launched_at"] = data["LaunchedAt"]
    if "TerminatedAt" in data:
        out["terminated_at"] = data["TerminatedAt"]
    return out
