"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#DeleteRecoveryGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string


class DeleteRecoveryGroupRequest(TypedDict, closed=True):
    recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string"
    """<p>The name of a recovery group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecoveryGroupRequest:
    out: DeleteRecoveryGroupRequest = {}  # type: ignore[typeddict-item]
    return out
