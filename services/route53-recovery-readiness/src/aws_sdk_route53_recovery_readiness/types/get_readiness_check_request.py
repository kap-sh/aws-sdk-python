"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetReadinessCheckRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class GetReadinessCheckRequest(TypedDict):
    readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a readiness check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadinessCheckRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadinessCheckRequest:
    out: GetReadinessCheckRequest = {}  # type: ignore[typeddict-item]
    return out
