"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#DeleteCrossAccountAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class DeleteCrossAccountAuthorizationRequest(TypedDict):
    cross_account_authorization: (
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    )
    """<p>The cross-account authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCrossAccountAuthorizationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCrossAccountAuthorizationRequest:
    out: DeleteCrossAccountAuthorizationRequest = {}  # type: ignore[typeddict-item]
    return out
