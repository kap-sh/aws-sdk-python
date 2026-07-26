"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationAccessScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.scope


class GetApplicationAccessScopeRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the access scope that you want to retrieve.</p>"""
    scope: "capo_sso_admin.types.scope.Scope"
    """<p>Specifies the name of the access scope for which you want the authorized targets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationAccessScopeRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["Scope"] = value["scope"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationAccessScopeRequest:
    out: GetApplicationAccessScopeRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "GetApplicationAccessScopeRequest.application_arn required"
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    else:
        raise DeserializationError("GetApplicationAccessScopeRequest.scope required")
    return out
