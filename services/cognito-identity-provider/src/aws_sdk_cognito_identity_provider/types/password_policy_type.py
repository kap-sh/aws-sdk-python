"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordPolicyType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.boolean_type
    import aws_sdk_cognito_identity_provider.types.password_history_size_type
    import aws_sdk_cognito_identity_provider.types.password_policy_min_length_type
    import aws_sdk_cognito_identity_provider.types.temporary_password_validity_days_type


class PasswordPolicyType(TypedDict):
    minimum_length: NotRequired[
        "aws_sdk_cognito_identity_provider.types.password_policy_min_length_type.PasswordPolicyMinLengthType"
    ]
    """<p>The minimum length of the password in the policy that you have set. This value can't be less than 6.</p>"""
    require_uppercase: (
        "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>The requirement in a password policy that users must include at least one uppercase letter in their password.</p>"""
    require_lowercase: (
        "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>The requirement in a password policy that users must include at least one lowercase letter in their password.</p>"""
    require_numbers: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>The requirement in a password policy that users must include at least one number in their password.</p>"""
    require_symbols: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>The requirement in a password policy that users must include at least one symbol in their password.</p>"""
    password_history_size: NotRequired[
        "aws_sdk_cognito_identity_provider.types.password_history_size_type.PasswordHistorySizeType"
    ]
    """<p>The number of previous passwords that you want Amazon Cognito to restrict each user from reusing. Users can't set a password that matches any of <code>n</code> previous passwords, where <code>n</code> is the value of <code>PasswordHistorySize</code>.</p>"""
    temporary_password_validity_days: "aws_sdk_cognito_identity_provider.types.temporary_password_validity_days_type.TemporaryPasswordValidityDaysType"
    """<p>The number of days a temporary password is valid in the password policy. If the user doesn't sign in during this time, an administrator must reset their password. Defaults to <code>7</code>. If you submit a value of <code>0</code>, Amazon Cognito treats it as a null value and sets <code>TemporaryPasswordValidityDays</code> to its default value.</p> <note> <p>When you set <code>TemporaryPasswordValidityDays</code> for a user pool, you can no longer set a value for the legacy <code>UnusedAccountValidityDays</code> parameter in that user pool.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PasswordPolicyType) -> dict:
    out: dict = {}
    if "minimum_length" in value:
        out["MinimumLength"] = value["minimum_length"]
    out["RequireUppercase"] = value.get("require_uppercase", False)
    out["RequireLowercase"] = value.get("require_lowercase", False)
    out["RequireNumbers"] = value.get("require_numbers", False)
    out["RequireSymbols"] = value.get("require_symbols", False)
    if "password_history_size" in value:
        out["PasswordHistorySize"] = value["password_history_size"]
    out["TemporaryPasswordValidityDays"] = value.get(
        "temporary_password_validity_days", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PasswordPolicyType:
    out: PasswordPolicyType = {}  # type: ignore[typeddict-item]
    if "MinimumLength" in data:
        out["minimum_length"] = data["MinimumLength"]
    if "RequireUppercase" in data:
        out["require_uppercase"] = data["RequireUppercase"]
    else:
        out["require_uppercase"] = False
    if "RequireLowercase" in data:
        out["require_lowercase"] = data["RequireLowercase"]
    else:
        out["require_lowercase"] = False
    if "RequireNumbers" in data:
        out["require_numbers"] = data["RequireNumbers"]
    else:
        out["require_numbers"] = False
    if "RequireSymbols" in data:
        out["require_symbols"] = data["RequireSymbols"]
    else:
        out["require_symbols"] = False
    if "PasswordHistorySize" in data:
        out["password_history_size"] = data["PasswordHistorySize"]
    if "TemporaryPasswordValidityDays" in data:
        out["temporary_password_validity_days"] = data["TemporaryPasswordValidityDays"]
    else:
        out["temporary_password_validity_days"] = 0
    return out
