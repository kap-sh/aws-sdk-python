"""Generated from Smithy shape ``com.amazonaws.mgn#CodeGenerationOutputFormatStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.code_generation_output_format_status
    import aws_sdk_mgn.types.large_bounded_string


class CodeGenerationOutputFormatStatusDetails(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_mgn.types.code_generation_output_format_status.CodeGenerationOutputFormatStatus"
    ]
    """<p>The status of the code generation for this output format.</p>"""
    status_detail_list: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>A list of detailed status information for the code generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeGenerationOutputFormatStatusDetails) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "status_detail_list" in value:
        out["statusDetailList"] = value["status_detail_list"]
    return out


def deserialize_json(data: dict) -> CodeGenerationOutputFormatStatusDetails:
    out: CodeGenerationOutputFormatStatusDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "statusDetailList" in data:
        out["status_detail_list"] = data["statusDetailList"]
    return out
