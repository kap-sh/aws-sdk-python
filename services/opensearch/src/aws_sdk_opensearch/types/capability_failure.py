"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.capability_failure_details
    import aws_sdk_opensearch.types.capability_failure_reason


class CapabilityFailure(TypedDict):
    reason: NotRequired[
        "aws_sdk_opensearch.types.capability_failure_reason.CapabilityFailureReason"
    ]
    """<p>The reason for the capability failure. Possible values: <code>KMS_KEY_INSUFFICIENT_PERMISSION</code>.</p>"""
    details: NotRequired[
        "aws_sdk_opensearch.types.capability_failure_details.CapabilityFailureDetails"
    ]
    """<p>Additional details about the capability failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityFailure) -> dict:
    out: dict = {}
    if "reason" in value:
        import aws_sdk_opensearch.types.capability_failure_reason

        out["reason"] = (
            aws_sdk_opensearch.types.capability_failure_reason.serialize_json(
                value["reason"]
            )
        )
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_json(data: dict) -> CapabilityFailure:
    out: CapabilityFailure = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        import aws_sdk_opensearch.types.capability_failure_reason

        out["reason"] = (
            aws_sdk_opensearch.types.capability_failure_reason.deserialize_json(
                data["reason"]
            )
        )
    if "details" in data:
        out["details"] = data["details"]
    return out
