"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.arn_list
    import aws_sdk_license_manager.types.client_token
    import aws_sdk_license_manager.types.integer
    import aws_sdk_license_manager.types.max_size3_string_list


class CreateTokenRequest(TypedDict, closed=True):
    license_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license. The ARN is mapped to the aud claim of the JWT token.</p>"""
    role_arns: NotRequired["aws_sdk_license_manager.types.arn_list.ArnList"]
    """<p>Amazon Resource Name (ARN) of the IAM roles to embed in the token. License Manager does not check whether the roles are in use.</p>"""
    expiration_in_days: NotRequired["aws_sdk_license_manager.types.integer.Integer"]
    """<p>Token expiration, in days, counted from token creation. The default is 365 days.</p>"""
    token_properties: NotRequired[
        "aws_sdk_license_manager.types.max_size3_string_list.MaxSize3StringList"
    ]
    """<p>Data specified by the caller to be included in the JWT token. The data is mapped to the amr claim of the JWT token.</p>"""
    client_token: "aws_sdk_license_manager.types.client_token.ClientToken"
    """<p>Idempotency token, valid for 10 minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTokenRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    if "role_arns" in value:
        import aws_sdk_license_manager.types.arn_list

        out["RoleArns"] = aws_sdk_license_manager.types.arn_list.serialize_aws_json_1_1(
            value["role_arns"]
        )
    if "expiration_in_days" in value:
        out["ExpirationInDays"] = value["expiration_in_days"]
    if "token_properties" in value:
        import aws_sdk_license_manager.types.max_size3_string_list

        out["TokenProperties"] = (
            aws_sdk_license_manager.types.max_size3_string_list.serialize_aws_json_1_1(
                value["token_properties"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTokenRequest:
    out: CreateTokenRequest = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("CreateTokenRequest.license_arn required")
    if "RoleArns" in data:
        import aws_sdk_license_manager.types.arn_list

        out["role_arns"] = (
            aws_sdk_license_manager.types.arn_list.deserialize_aws_json_1_1(
                data["RoleArns"]
            )
        )
    if "ExpirationInDays" in data:
        out["expiration_in_days"] = data["ExpirationInDays"]
    if "TokenProperties" in data:
        import aws_sdk_license_manager.types.max_size3_string_list

        out["token_properties"] = (
            aws_sdk_license_manager.types.max_size3_string_list.deserialize_aws_json_1_1(
                data["TokenProperties"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateTokenRequest.client_token required")
    return out
