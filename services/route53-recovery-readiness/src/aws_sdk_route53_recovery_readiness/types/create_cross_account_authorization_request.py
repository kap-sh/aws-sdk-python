"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#CreateCrossAccountAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.cross_account_authorization


class CreateCrossAccountAuthorizationRequest(TypedDict):
    cross_account_authorization: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization"
    ]
    """<p>The cross-account authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCrossAccountAuthorizationRequest) -> dict:
    out: dict = {}
    if "cross_account_authorization" in value:
        out["crossAccountAuthorization"] = value["cross_account_authorization"]
    return out


def deserialize_json(data: dict) -> CreateCrossAccountAuthorizationRequest:
    out: CreateCrossAccountAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if "crossAccountAuthorization" in data:
        out["cross_account_authorization"] = data["crossAccountAuthorization"]
    return out
