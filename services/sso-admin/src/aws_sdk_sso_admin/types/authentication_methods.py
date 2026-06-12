"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.authentication_method_item

AuthenticationMethods: TypeAlias = list[
    "aws_sdk_sso_admin.types.authentication_method_item.AuthenticationMethodItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMethods) -> list:
    import aws_sdk_sso_admin.types.authentication_method_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.authentication_method_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AuthenticationMethods:
    import aws_sdk_sso_admin.types.authentication_method_item

    out: AuthenticationMethods = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.authentication_method_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
