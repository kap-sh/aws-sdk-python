"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethodItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.authentication_method
    import capo_sso_admin.types.authentication_method_type


class AuthenticationMethodItem(TypedDict, closed=True):
    authentication_method_type: NotRequired[
        "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType"
    ]
    """<p>The type of authentication that is used by this method.</p>"""
    authentication_method: NotRequired[
        "capo_sso_admin.types.authentication_method.AuthenticationMethod"
    ]
    """<p>A structure that describes an authentication method. The contents of this structure is determined by the <code>AuthenticationMethodType</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMethodItem) -> dict:
    out: dict = {}
    if "authentication_method_type" in value:
        import capo_sso_admin.types.authentication_method_type

        out["AuthenticationMethodType"] = (
            capo_sso_admin.types.authentication_method_type.serialize_aws_json_1_1(
                value["authentication_method_type"]
            )
        )
    if "authentication_method" in value:
        import capo_sso_admin.types.authentication_method

        out["AuthenticationMethod"] = (
            capo_sso_admin.types.authentication_method.serialize_aws_json_1_1(
                value["authentication_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationMethodItem:
    out: AuthenticationMethodItem = {}  # type: ignore[typeddict-item]
    if "AuthenticationMethodType" in data:
        import capo_sso_admin.types.authentication_method_type

        out["authentication_method_type"] = (
            capo_sso_admin.types.authentication_method_type.deserialize_aws_json_1_1(
                data["AuthenticationMethodType"]
            )
        )
    if "AuthenticationMethod" in data:
        import capo_sso_admin.types.authentication_method

        out["authentication_method"] = (
            capo_sso_admin.types.authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    return out
