"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetRandomPasswordRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.exclude_characters_type
    import aws_sdk_secrets_manager.types.exclude_lowercase_type
    import aws_sdk_secrets_manager.types.exclude_numbers_type
    import aws_sdk_secrets_manager.types.exclude_punctuation_type
    import aws_sdk_secrets_manager.types.exclude_uppercase_type
    import aws_sdk_secrets_manager.types.include_space_type
    import aws_sdk_secrets_manager.types.password_length_type
    import aws_sdk_secrets_manager.types.require_each_included_type_type


class GetRandomPasswordRequest(TypedDict):
    password_length: NotRequired[
        "aws_sdk_secrets_manager.types.password_length_type.PasswordLengthType"
    ]
    """<p>The length of the password. If you don't include this parameter, the default length is 32 characters.</p>"""
    exclude_characters: NotRequired[
        "aws_sdk_secrets_manager.types.exclude_characters_type.ExcludeCharactersType"
    ]
    """<p>A string of the characters that you don't want in the password.</p>"""
    exclude_numbers: NotRequired[
        "aws_sdk_secrets_manager.types.exclude_numbers_type.ExcludeNumbersType"
    ]
    """<p>Specifies whether to exclude numbers from the password. If you don't include this switch, the password can contain numbers.</p>"""
    exclude_punctuation: NotRequired[
        "aws_sdk_secrets_manager.types.exclude_punctuation_type.ExcludePunctuationType"
    ]
    """<p>Specifies whether to exclude the following punctuation characters from the password: <code>! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~</code>. If you don't include this switch, the password can contain punctuation.</p>"""
    exclude_uppercase: NotRequired[
        "aws_sdk_secrets_manager.types.exclude_uppercase_type.ExcludeUppercaseType"
    ]
    """<p>Specifies whether to exclude uppercase letters from the password. If you don't include this switch, the password can contain uppercase letters.</p>"""
    exclude_lowercase: NotRequired[
        "aws_sdk_secrets_manager.types.exclude_lowercase_type.ExcludeLowercaseType"
    ]
    """<p>Specifies whether to exclude lowercase letters from the password. If you don't include this switch, the password can contain lowercase letters.</p>"""
    include_space: NotRequired[
        "aws_sdk_secrets_manager.types.include_space_type.IncludeSpaceType"
    ]
    """<p>Specifies whether to include the space character. If you include this switch, the password can contain space characters.</p>"""
    require_each_included_type: NotRequired[
        "aws_sdk_secrets_manager.types.require_each_included_type_type.RequireEachIncludedTypeType"
    ]
    """<p>Specifies whether to include at least one upper and lowercase letter, one number, and one punctuation. If you don't include this switch, the password contains at least one of every character type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRandomPasswordRequest) -> dict:
    out: dict = {}
    if "password_length" in value:
        out["PasswordLength"] = value["password_length"]
    if "exclude_characters" in value:
        out["ExcludeCharacters"] = value["exclude_characters"]
    if "exclude_numbers" in value:
        out["ExcludeNumbers"] = value["exclude_numbers"]
    if "exclude_punctuation" in value:
        out["ExcludePunctuation"] = value["exclude_punctuation"]
    if "exclude_uppercase" in value:
        out["ExcludeUppercase"] = value["exclude_uppercase"]
    if "exclude_lowercase" in value:
        out["ExcludeLowercase"] = value["exclude_lowercase"]
    if "include_space" in value:
        out["IncludeSpace"] = value["include_space"]
    if "require_each_included_type" in value:
        out["RequireEachIncludedType"] = value["require_each_included_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRandomPasswordRequest:
    out: GetRandomPasswordRequest = {}  # type: ignore[typeddict-item]
    if "PasswordLength" in data:
        out["password_length"] = data["PasswordLength"]
    if "ExcludeCharacters" in data:
        out["exclude_characters"] = data["ExcludeCharacters"]
    if "ExcludeNumbers" in data:
        out["exclude_numbers"] = data["ExcludeNumbers"]
    if "ExcludePunctuation" in data:
        out["exclude_punctuation"] = data["ExcludePunctuation"]
    if "ExcludeUppercase" in data:
        out["exclude_uppercase"] = data["ExcludeUppercase"]
    if "ExcludeLowercase" in data:
        out["exclude_lowercase"] = data["ExcludeLowercase"]
    if "IncludeSpace" in data:
        out["include_space"] = data["IncludeSpace"]
    if "RequireEachIncludedType" in data:
        out["require_each_included_type"] = data["RequireEachIncludedType"]
    return out
