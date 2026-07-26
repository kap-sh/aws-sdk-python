"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListCrossAccountAuthorizationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_cross_account_authorization
    import capo_route53_recovery_readiness.types.__string


class ListCrossAccountAuthorizationsResponse(TypedDict, closed=True):
    cross_account_authorizations: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_cross_account_authorization.__listOfCrossAccountAuthorization"
    ]
    """<p>A list of cross-account authorizations.</p>"""
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCrossAccountAuthorizationsResponse) -> dict:
    out: dict = {}
    if "cross_account_authorizations" in value:
        import capo_route53_recovery_readiness.types.__list_of_cross_account_authorization

        out["crossAccountAuthorizations"] = (
            capo_route53_recovery_readiness.types.__list_of_cross_account_authorization.serialize_json(
                value["cross_account_authorizations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCrossAccountAuthorizationsResponse:
    out: ListCrossAccountAuthorizationsResponse = {}  # type: ignore[typeddict-item]
    if "crossAccountAuthorizations" in data:
        import capo_route53_recovery_readiness.types.__list_of_cross_account_authorization

        out["cross_account_authorizations"] = (
            capo_route53_recovery_readiness.types.__list_of_cross_account_authorization.deserialize_json(
                data["crossAccountAuthorizations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
