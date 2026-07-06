"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationAssignmentForPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.principal_id
    import aws_sdk_sso_admin.types.principal_type


class ApplicationAssignmentForPrincipal(TypedDict, closed=True):
    application_arn: NotRequired[
        "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    ]
    """<p>The ARN of the application to which the specified principal is assigned.</p>"""
    principal_id: NotRequired["aws_sdk_sso_admin.types.principal_id.PrincipalId"]
    """<p>The unique identifier of the principal assigned to the application.</p>"""
    principal_type: NotRequired["aws_sdk_sso_admin.types.principal_type.PrincipalType"]
    """<p>The type of the principal assigned to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssignmentForPrincipal) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "principal_type" in value:
        import aws_sdk_sso_admin.types.principal_type

        out["PrincipalType"] = (
            aws_sdk_sso_admin.types.principal_type.serialize_aws_json_1_1(
                value["principal_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationAssignmentForPrincipal:
    out: ApplicationAssignmentForPrincipal = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "PrincipalType" in data:
        import aws_sdk_sso_admin.types.principal_type

        out["principal_type"] = (
            aws_sdk_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    return out
