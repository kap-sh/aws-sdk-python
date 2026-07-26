"""Generated from Smithy shape ``com.amazonaws.finspacedata#ChangesetErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.error_category
    import capo_finspace_data.types.error_message


class ChangesetErrorInfo(TypedDict, closed=True):
    error_message: NotRequired["capo_finspace_data.types.error_message.ErrorMessage"]
    """<p>The text of the error message.</p>"""
    error_category: NotRequired["capo_finspace_data.types.error_category.ErrorCategory"]
    """<p>The category of the error.</p> <ul> <li> <p> <code>VALIDATION</code> – The inputs to this request are invalid.</p> </li> <li> <p> <code>SERVICE_QUOTA_EXCEEDED</code> – Service quotas have been exceeded. Please contact AWS support to increase quotas.</p> </li> <li> <p> <code>ACCESS_DENIED</code> – Missing required permission to perform this request.</p> </li> <li> <p> <code>RESOURCE_NOT_FOUND</code> – One or more inputs to this request were not found.</p> </li> <li> <p> <code>THROTTLING</code> – The system temporarily lacks sufficient resources to process the request.</p> </li> <li> <p> <code>INTERNAL_SERVICE_EXCEPTION</code> – An internal service error has occurred.</p> </li> <li> <p> <code>CANCELLED</code> – Cancelled.</p> </li> <li> <p> <code>USER_RECOVERABLE</code> – A user recoverable error has occurred.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangesetErrorInfo) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_category" in value:
        import capo_finspace_data.types.error_category

        out["errorCategory"] = capo_finspace_data.types.error_category.serialize_json(
            value["error_category"]
        )
    return out


def deserialize_json(data: dict) -> ChangesetErrorInfo:
    out: ChangesetErrorInfo = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCategory" in data:
        import capo_finspace_data.types.error_category

        out["error_category"] = (
            capo_finspace_data.types.error_category.deserialize_json(
                data["errorCategory"]
            )
        )
    return out
