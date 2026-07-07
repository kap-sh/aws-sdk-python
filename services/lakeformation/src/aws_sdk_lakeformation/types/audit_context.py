"""Generated from Smithy shape ``com.amazonaws.lakeformation#AuditContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.audit_context_string


class AuditContext(TypedDict, closed=True):
    additional_audit_context: NotRequired[
        "aws_sdk_lakeformation.types.audit_context_string.AuditContextString"
    ]
    """<p>The filter engine can populate the 'AdditionalAuditContext' information with the request ID for you to track. This information will be displayed in CloudTrail log in your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditContext) -> dict:
    out: dict = {}
    if "additional_audit_context" in value:
        out["AdditionalAuditContext"] = value["additional_audit_context"]
    return out


def deserialize_json(data: dict) -> AuditContext:
    out: AuditContext = {}  # type: ignore[typeddict-item]
    if "AdditionalAuditContext" in data:
        out["additional_audit_context"] = data["AdditionalAuditContext"]
    return out
