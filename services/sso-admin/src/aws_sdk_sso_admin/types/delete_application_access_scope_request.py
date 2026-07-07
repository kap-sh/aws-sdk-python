"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteApplicationAccessScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.scope


class DeleteApplicationAccessScopeRequest(TypedDict, closed=True):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the access scope to delete.</p>"""
    scope: "aws_sdk_sso_admin.types.scope.Scope"
    """<p>Specifies the name of the access scope to remove from the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationAccessScopeRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["Scope"] = value["scope"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationAccessScopeRequest:
    out: DeleteApplicationAccessScopeRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "DeleteApplicationAccessScopeRequest.application_arn required"
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    else:
        raise DeserializationError("DeleteApplicationAccessScopeRequest.scope required")
    return out
