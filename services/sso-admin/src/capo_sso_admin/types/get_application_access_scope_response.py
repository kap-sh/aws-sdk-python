"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationAccessScopeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.scope
    import capo_sso_admin.types.scope_targets


class GetApplicationAccessScopeResponse(TypedDict, closed=True):
    scope: "capo_sso_admin.types.scope.Scope"
    """<p>The name of the access scope that can be used with the authorized targets.</p>"""
    authorized_targets: NotRequired["capo_sso_admin.types.scope_targets.ScopeTargets"]
    """<p>An array of authorized targets associated with this access scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationAccessScopeResponse) -> dict:
    out: dict = {}
    out["Scope"] = value["scope"]
    if "authorized_targets" in value:
        import capo_sso_admin.types.scope_targets

        out["AuthorizedTargets"] = (
            capo_sso_admin.types.scope_targets.serialize_aws_json_1_1(
                value["authorized_targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationAccessScopeResponse:
    out: GetApplicationAccessScopeResponse = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        out["scope"] = data["Scope"]
    else:
        raise DeserializationError("GetApplicationAccessScopeResponse.scope required")
    if "AuthorizedTargets" in data:
        import capo_sso_admin.types.scope_targets

        out["authorized_targets"] = (
            capo_sso_admin.types.scope_targets.deserialize_aws_json_1_1(
                data["AuthorizedTargets"]
            )
        )
    return out
