"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#DeleteReadinessCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class DeleteReadinessCheckRequest(TypedDict, closed=True):
    readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a readiness check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReadinessCheckRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReadinessCheckRequest:
    out: DeleteReadinessCheckRequest = {}  # type: ignore[typeddict-item]
    return out
