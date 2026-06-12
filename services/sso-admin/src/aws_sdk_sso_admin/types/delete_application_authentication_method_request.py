"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteApplicationAuthenticationMethodRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.authentication_method_type


class DeleteApplicationAuthenticationMethodRequest(TypedDict):
    application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the authentication method to delete.</p>"""
    authentication_method_type: (
        "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType"
    )
    """<p>Specifies the authentication method type to delete from the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationAuthenticationMethodRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import aws_sdk_sso_admin.types.authentication_method_type

    out["AuthenticationMethodType"] = (
        aws_sdk_sso_admin.types.authentication_method_type.serialize_aws_json_1_1(
            value["authentication_method_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteApplicationAuthenticationMethodRequest:
    out: DeleteApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "DeleteApplicationAuthenticationMethodRequest.application_arn required"
        )
    if "AuthenticationMethodType" in data:
        import aws_sdk_sso_admin.types.authentication_method_type

        out["authentication_method_type"] = (
            aws_sdk_sso_admin.types.authentication_method_type.deserialize_aws_json_1_1(
                data["AuthenticationMethodType"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteApplicationAuthenticationMethodRequest.authentication_method_type required"
        )
    return out
