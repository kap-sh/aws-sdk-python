"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ScopeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.scope
    import aws_sdk_sso_admin.types.scope_targets


class ScopeDetails(TypedDict):
    scope: "aws_sdk_sso_admin.types.scope.Scope"
    """<p>The name of the access scope.</p>"""
    authorized_targets: NotRequired[
        "aws_sdk_sso_admin.types.scope_targets.ScopeTargets"
    ]
    """<p>An array list of ARNs of applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeDetails) -> dict:
    out: dict = {}
    out["Scope"] = value["scope"]
    if "authorized_targets" in value:
        import aws_sdk_sso_admin.types.scope_targets

        out["AuthorizedTargets"] = (
            aws_sdk_sso_admin.types.scope_targets.serialize_aws_json_1_1(
                value["authorized_targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScopeDetails:
    out: ScopeDetails = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        out["scope"] = data["Scope"]
    else:
        raise DeserializationError("ScopeDetails.scope required")
    if "AuthorizedTargets" in data:
        import aws_sdk_sso_admin.types.scope_targets

        out["authorized_targets"] = (
            aws_sdk_sso_admin.types.scope_targets.deserialize_aws_json_1_1(
                data["AuthorizedTargets"]
            )
        )
    return out
