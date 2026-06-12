"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteApplicationGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.grant_type


class DeleteApplicationGrantRequest(TypedDict):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the grant to delete.</p>"""
    grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType"
    """<p>Specifies the type of grant to delete from the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationGrantRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import aws_sdk_sso_admin.types.grant_type

    out["GrantType"] = aws_sdk_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationGrantRequest:
    out: DeleteApplicationGrantRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "DeleteApplicationGrantRequest.application_arn required"
        )
    if "GrantType" in data:
        import aws_sdk_sso_admin.types.grant_type

        out["grant_type"] = aws_sdk_sso_admin.types.grant_type.deserialize_aws_json_1_1(
            data["GrantType"]
        )
    else:
        raise DeserializationError("DeleteApplicationGrantRequest.grant_type required")
    return out
