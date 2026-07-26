"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.status_reason_code


class StandardsStatusReason(TypedDict, closed=True):
    status_reason_code: NotRequired[
        "capo_securityhub.types.status_reason_code.StatusReasonCode"
    ]
    """<p>The reason code that represents the reason for the current status of a standard subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsStatusReason) -> dict:
    out: dict = {}
    if "status_reason_code" in value:
        import capo_securityhub.types.status_reason_code

        out["StatusReasonCode"] = (
            capo_securityhub.types.status_reason_code.serialize_json(
                value["status_reason_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardsStatusReason:
    out: StandardsStatusReason = {}  # type: ignore[typeddict-item]
    if "StatusReasonCode" in data:
        import capo_securityhub.types.status_reason_code

        out["status_reason_code"] = (
            capo_securityhub.types.status_reason_code.deserialize_json(
                data["StatusReasonCode"]
            )
        )
    return out
