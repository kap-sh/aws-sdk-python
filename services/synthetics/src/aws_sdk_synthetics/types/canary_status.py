"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_state
    import aws_sdk_synthetics.types.canary_state_reason_code
    import aws_sdk_synthetics.types.string


class CanaryStatus(TypedDict):
    state: NotRequired["aws_sdk_synthetics.types.canary_state.CanaryState"]
    """<p>The current state of the canary.</p>"""
    state_reason: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>If the canary creation or update failed, this field provides details on the failure.</p>"""
    state_reason_code: NotRequired[
        "aws_sdk_synthetics.types.canary_state_reason_code.CanaryStateReasonCode"
    ]
    """<p>If the canary creation or update failed, this field displays the reason code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_synthetics.types.canary_state

        out["State"] = aws_sdk_synthetics.types.canary_state.serialize_json(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_code" in value:
        import aws_sdk_synthetics.types.canary_state_reason_code

        out["StateReasonCode"] = (
            aws_sdk_synthetics.types.canary_state_reason_code.serialize_json(
                value["state_reason_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> CanaryStatus:
    out: CanaryStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_synthetics.types.canary_state

        out["state"] = aws_sdk_synthetics.types.canary_state.deserialize_json(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "StateReasonCode" in data:
        import aws_sdk_synthetics.types.canary_state_reason_code

        out["state_reason_code"] = (
            aws_sdk_synthetics.types.canary_state_reason_code.deserialize_json(
                data["StateReasonCode"]
            )
        )
    return out
