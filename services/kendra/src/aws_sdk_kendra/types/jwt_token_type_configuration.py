"""Generated from Smithy shape ``com.amazonaws.kendra#JwtTokenTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.claim_regex
    import aws_sdk_kendra.types.group_attribute_field
    import aws_sdk_kendra.types.issuer
    import aws_sdk_kendra.types.key_location
    import aws_sdk_kendra.types.role_arn
    import aws_sdk_kendra.types.url
    import aws_sdk_kendra.types.user_name_attribute_field


class JwtTokenTypeConfiguration(TypedDict, closed=True):
    key_location: "aws_sdk_kendra.types.key_location.KeyLocation"
    """<p>The location of the key.</p>"""
    url: NotRequired["aws_sdk_kendra.types.url.Url"]
    """<p>The signing key URL.</p>"""
    secret_manager_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (arn) of the secret.</p>"""
    user_name_attribute_field: NotRequired[
        "aws_sdk_kendra.types.user_name_attribute_field.UserNameAttributeField"
    ]
    """<p>The user name attribute field.</p>"""
    group_attribute_field: NotRequired[
        "aws_sdk_kendra.types.group_attribute_field.GroupAttributeField"
    ]
    """<p>The group attribute field.</p>"""
    issuer: NotRequired["aws_sdk_kendra.types.issuer.Issuer"]
    """<p>The issuer of the token.</p>"""
    claim_regex: NotRequired["aws_sdk_kendra.types.claim_regex.ClaimRegex"]
    """<p>The regular expression that identifies the claim.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JwtTokenTypeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.key_location

    out["KeyLocation"] = aws_sdk_kendra.types.key_location.serialize_aws_json_1_1(
        value["key_location"]
    )
    if "url" in value:
        out["URL"] = value["url"]
    if "secret_manager_arn" in value:
        out["SecretManagerArn"] = value["secret_manager_arn"]
    if "user_name_attribute_field" in value:
        out["UserNameAttributeField"] = value["user_name_attribute_field"]
    if "group_attribute_field" in value:
        out["GroupAttributeField"] = value["group_attribute_field"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "claim_regex" in value:
        out["ClaimRegex"] = value["claim_regex"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JwtTokenTypeConfiguration:
    out: JwtTokenTypeConfiguration = {}  # type: ignore[typeddict-item]
    if "KeyLocation" in data:
        import aws_sdk_kendra.types.key_location

        out["key_location"] = (
            aws_sdk_kendra.types.key_location.deserialize_aws_json_1_1(
                data["KeyLocation"]
            )
        )
    else:
        raise DeserializationError("JwtTokenTypeConfiguration.key_location required")
    if "URL" in data:
        out["url"] = data["URL"]
    if "SecretManagerArn" in data:
        out["secret_manager_arn"] = data["SecretManagerArn"]
    if "UserNameAttributeField" in data:
        out["user_name_attribute_field"] = data["UserNameAttributeField"]
    if "GroupAttributeField" in data:
        out["group_attribute_field"] = data["GroupAttributeField"]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    if "ClaimRegex" in data:
        out["claim_regex"] = data["ClaimRegex"]
    return out
