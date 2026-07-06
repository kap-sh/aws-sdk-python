"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.principal_id
    import aws_sdk_sso_admin.types.principal_type


class ApplicationAssignment(TypedDict, closed=True):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>The ARN of the application that has principals assigned.</p>"""
    principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId"
    """<p>The unique identifier of the principal assigned to the application.</p>"""
    principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType"
    """<p>The type of the principal assigned to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssignment) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["PrincipalId"] = value["principal_id"]
    import aws_sdk_sso_admin.types.principal_type

    out["PrincipalType"] = (
        aws_sdk_sso_admin.types.principal_type.serialize_aws_json_1_1(
            value["principal_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationAssignment:
    out: ApplicationAssignment = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError("ApplicationAssignment.application_arn required")
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    else:
        raise DeserializationError("ApplicationAssignment.principal_id required")
    if "PrincipalType" in data:
        import aws_sdk_sso_admin.types.principal_type

        out["principal_type"] = (
            aws_sdk_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    else:
        raise DeserializationError("ApplicationAssignment.principal_type required")
    return out
