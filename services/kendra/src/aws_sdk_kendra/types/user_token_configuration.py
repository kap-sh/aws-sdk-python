"""Generated from Smithy shape ``com.amazonaws.kendra#UserTokenConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.json_token_type_configuration
    import aws_sdk_kendra.types.jwt_token_type_configuration


class UserTokenConfiguration(TypedDict, closed=True):
    jwt_token_type_configuration: NotRequired[
        "aws_sdk_kendra.types.jwt_token_type_configuration.JwtTokenTypeConfiguration"
    ]
    """<p>Information about the JWT token type configuration.</p>"""
    json_token_type_configuration: NotRequired[
        "aws_sdk_kendra.types.json_token_type_configuration.JsonTokenTypeConfiguration"
    ]
    """<p>Information about the JSON token type configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserTokenConfiguration) -> dict:
    out: dict = {}
    if "jwt_token_type_configuration" in value:
        import aws_sdk_kendra.types.jwt_token_type_configuration

        out["JwtTokenTypeConfiguration"] = (
            aws_sdk_kendra.types.jwt_token_type_configuration.serialize_aws_json_1_1(
                value["jwt_token_type_configuration"]
            )
        )
    if "json_token_type_configuration" in value:
        import aws_sdk_kendra.types.json_token_type_configuration

        out["JsonTokenTypeConfiguration"] = (
            aws_sdk_kendra.types.json_token_type_configuration.serialize_aws_json_1_1(
                value["json_token_type_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserTokenConfiguration:
    out: UserTokenConfiguration = {}  # type: ignore[typeddict-item]
    if "JwtTokenTypeConfiguration" in data:
        import aws_sdk_kendra.types.jwt_token_type_configuration

        out["jwt_token_type_configuration"] = (
            aws_sdk_kendra.types.jwt_token_type_configuration.deserialize_aws_json_1_1(
                data["JwtTokenTypeConfiguration"]
            )
        )
    if "JsonTokenTypeConfiguration" in data:
        import aws_sdk_kendra.types.json_token_type_configuration

        out["json_token_type_configuration"] = (
            aws_sdk_kendra.types.json_token_type_configuration.deserialize_aws_json_1_1(
                data["JsonTokenTypeConfiguration"]
            )
        )
    return out
