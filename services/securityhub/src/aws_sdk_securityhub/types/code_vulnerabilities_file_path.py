"""Generated from Smithy shape ``com.amazonaws.securityhub#CodeVulnerabilitiesFilePath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class CodeVulnerabilitiesFilePath(TypedDict, closed=True):
    end_line: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The line number of the last line of code in which the vulnerability is located. </p>"""
    file_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the file in which the code vulnerability is located. </p>"""
    file_path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The file path to the code in which the vulnerability is located. </p>"""
    start_line: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The line number of the first line of code in which the vulnerability is located. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeVulnerabilitiesFilePath) -> dict:
    out: dict = {}
    if "end_line" in value:
        out["EndLine"] = value["end_line"]
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    if "file_path" in value:
        out["FilePath"] = value["file_path"]
    if "start_line" in value:
        out["StartLine"] = value["start_line"]
    return out


def deserialize_json(data: dict) -> CodeVulnerabilitiesFilePath:
    out: CodeVulnerabilitiesFilePath = {}  # type: ignore[typeddict-item]
    if "EndLine" in data:
        out["end_line"] = data["EndLine"]
    if "FileName" in data:
        out["file_name"] = data["FileName"]
    if "FilePath" in data:
        out["file_path"] = data["FilePath"]
    if "StartLine" in data:
        out["start_line"] = data["StartLine"]
    return out
