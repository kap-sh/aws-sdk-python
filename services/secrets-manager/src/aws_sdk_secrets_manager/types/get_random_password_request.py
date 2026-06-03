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
    exclude_numbers: (
        "aws_sdk_secrets_manager.types.exclude_numbers_type.ExcludeNumbersType"
    )
    """<p>Specifies whether to exclude numbers from the password. If you don't include this switch, the password can contain numbers.</p>"""
    exclude_punctuation: (
        "aws_sdk_secrets_manager.types.exclude_punctuation_type.ExcludePunctuationType"
    )
    """<p>Specifies whether to exclude the following punctuation characters from the password: <code>! \" # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~</code>. If you don't include this switch, the password can contain punctuation.</p>"""
    exclude_uppercase: (
        "aws_sdk_secrets_manager.types.exclude_uppercase_type.ExcludeUppercaseType"
    )
    """<p>Specifies whether to exclude uppercase letters from the password. If you don't include this switch, the password can contain uppercase letters.</p>"""
    exclude_lowercase: (
        "aws_sdk_secrets_manager.types.exclude_lowercase_type.ExcludeLowercaseType"
    )
    """<p>Specifies whether to exclude lowercase letters from the password. If you don't include this switch, the password can contain lowercase letters.</p>"""
    include_space: "aws_sdk_secrets_manager.types.include_space_type.IncludeSpaceType"
    """<p>Specifies whether to include the space character. If you include this switch, the password can contain space characters.</p>"""
    require_each_included_type: "aws_sdk_secrets_manager.types.require_each_included_type_type.RequireEachIncludedTypeType"
    """<p>Specifies whether to include at least one upper and lowercase letter, one number, and one punctuation. If you don't include this switch, the password contains at least one of every character type.</p>"""
