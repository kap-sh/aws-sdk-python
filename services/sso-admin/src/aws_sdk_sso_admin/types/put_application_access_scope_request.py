"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationAccessScopeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.scope
    import aws_sdk_sso_admin.types.scope_targets


class PutApplicationAccessScopeRequest(TypedDict):
    scope: "aws_sdk_sso_admin.types.scope.Scope"
    """<p>Specifies the name of the access scope to be associated with the specified targets.</p>"""
    authorized_targets: NotRequired[
        "aws_sdk_sso_admin.types.scope_targets.ScopeTargets"
    ]
    """<p>Specifies an array list of ARNs that represent the authorized targets for this access scope.</p>"""
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the access scope with the targets to add or update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationAccessScopeRequest) -> dict:
    out: dict = {}
    out["Scope"] = value["scope"]
    if "authorized_targets" in value:
        import aws_sdk_sso_admin.types.scope_targets

        out["AuthorizedTargets"] = (
            aws_sdk_sso_admin.types.scope_targets.serialize_aws_json_1_1(
                value["authorized_targets"]
            )
        )
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationAccessScopeRequest:
    out: PutApplicationAccessScopeRequest = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        out["scope"] = data["Scope"]
    else:
        raise DeserializationError("PutApplicationAccessScopeRequest.scope required")
    if "AuthorizedTargets" in data:
        import aws_sdk_sso_admin.types.scope_targets

        out["authorized_targets"] = (
            aws_sdk_sso_admin.types.scope_targets.deserialize_aws_json_1_1(
                data["AuthorizedTargets"]
            )
        )
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "PutApplicationAccessScopeRequest.application_arn required"
        )
    return out
