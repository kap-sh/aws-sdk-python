"""Generated from Smithy shape ``com.amazonaws.securityhub#ClassificationStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class ClassificationStatus(TypedDict):
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The code that represents the status of the sensitive data detection.</p>"""
    reason: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A longer description of the current status of the sensitive data detection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationStatus) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ClassificationStatus:
    out: ClassificationStatus = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
