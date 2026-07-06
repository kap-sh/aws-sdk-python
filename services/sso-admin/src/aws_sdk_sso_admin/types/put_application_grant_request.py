"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.grant
    import aws_sdk_sso_admin.types.grant_type


class PutApplicationGrantRequest(TypedDict, closed=True):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application to update.</p>"""
    grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType"
    """<p>Specifies the type of grant to update.</p>"""
    grant: "aws_sdk_sso_admin.types.grant.Grant"
    """<p>Specifies a structure that describes the grant to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationGrantRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import aws_sdk_sso_admin.types.grant_type

    out["GrantType"] = aws_sdk_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    import aws_sdk_sso_admin.types.grant

    out["Grant"] = aws_sdk_sso_admin.types.grant.serialize_aws_json_1_1(value["grant"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationGrantRequest:
    out: PutApplicationGrantRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "PutApplicationGrantRequest.application_arn required"
        )
    if "GrantType" in data:
        import aws_sdk_sso_admin.types.grant_type

        out["grant_type"] = aws_sdk_sso_admin.types.grant_type.deserialize_aws_json_1_1(
            data["GrantType"]
        )
    else:
        raise DeserializationError("PutApplicationGrantRequest.grant_type required")
    if "Grant" in data:
        import aws_sdk_sso_admin.types.grant

        out["grant"] = aws_sdk_sso_admin.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    else:
        raise DeserializationError("PutApplicationGrantRequest.grant required")
    return out
