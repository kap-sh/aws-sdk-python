"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#CreateCrossAccountAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.cross_account_authorization


class CreateCrossAccountAuthorizationResponse(TypedDict, closed=True):
    cross_account_authorization: NotRequired[
        "capo_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization"
    ]
    """<p>The cross-account authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCrossAccountAuthorizationResponse) -> dict:
    out: dict = {}
    if "cross_account_authorization" in value:
        out["crossAccountAuthorization"] = value["cross_account_authorization"]
    return out


def deserialize_json(data: dict) -> CreateCrossAccountAuthorizationResponse:
    out: CreateCrossAccountAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "crossAccountAuthorization" in data:
        out["cross_account_authorization"] = data["crossAccountAuthorization"]
    return out
