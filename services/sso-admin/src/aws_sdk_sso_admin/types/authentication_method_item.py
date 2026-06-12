"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethodItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.authentication_method
    import aws_sdk_sso_admin.types.authentication_method_type


class AuthenticationMethodItem(TypedDict):
    authentication_method_type: NotRequired[
        "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType"
    ]
    """<p>The type of authentication that is used by this method.</p>"""
    authentication_method: NotRequired[
        "aws_sdk_sso_admin.types.authentication_method.AuthenticationMethod"
    ]
    """<p>A structure that describes an authentication method. The contents of this structure is determined by the <code>AuthenticationMethodType</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMethodItem) -> dict:
    out: dict = {}
    if "authentication_method_type" in value:
        import aws_sdk_sso_admin.types.authentication_method_type

        out["AuthenticationMethodType"] = (
            aws_sdk_sso_admin.types.authentication_method_type.serialize_aws_json_1_1(
                value["authentication_method_type"]
            )
        )
    if "authentication_method" in value:
        import aws_sdk_sso_admin.types.authentication_method

        out["AuthenticationMethod"] = (
            aws_sdk_sso_admin.types.authentication_method.serialize_aws_json_1_1(
                value["authentication_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationMethodItem:
    out: AuthenticationMethodItem = {}  # type: ignore[typeddict-item]
    if "AuthenticationMethodType" in data:
        import aws_sdk_sso_admin.types.authentication_method_type

        out["authentication_method_type"] = (
            aws_sdk_sso_admin.types.authentication_method_type.deserialize_aws_json_1_1(
                data["AuthenticationMethodType"]
            )
        )
    if "AuthenticationMethod" in data:
        import aws_sdk_sso_admin.types.authentication_method

        out["authentication_method"] = (
            aws_sdk_sso_admin.types.authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    return out
