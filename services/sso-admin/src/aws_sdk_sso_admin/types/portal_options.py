"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PortalOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_visibility
    import aws_sdk_sso_admin.types.sign_in_options


class PortalOptions(TypedDict):
    sign_in_options: NotRequired[
        "aws_sdk_sso_admin.types.sign_in_options.SignInOptions"
    ]
    """<p>A structure that describes the sign-in options for the access portal.</p>"""
    visibility: "aws_sdk_sso_admin.types.application_visibility.ApplicationVisibility"
    """<p>Indicates whether this application is visible in the access portal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortalOptions) -> dict:
    out: dict = {}
    if "sign_in_options" in value:
        import aws_sdk_sso_admin.types.sign_in_options

        out["SignInOptions"] = (
            aws_sdk_sso_admin.types.sign_in_options.serialize_aws_json_1_1(
                value["sign_in_options"]
            )
        )
    import aws_sdk_sso_admin.types.application_visibility

    out["Visibility"] = (
        aws_sdk_sso_admin.types.application_visibility.serialize_aws_json_1_1(
            value.get("visibility", "ENABLED")
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PortalOptions:
    out: PortalOptions = {}  # type: ignore[typeddict-item]
    if "SignInOptions" in data:
        import aws_sdk_sso_admin.types.sign_in_options

        out["sign_in_options"] = (
            aws_sdk_sso_admin.types.sign_in_options.deserialize_aws_json_1_1(
                data["SignInOptions"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_sso_admin.types.application_visibility

        out["visibility"] = (
            aws_sdk_sso_admin.types.application_visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    else:
        out["visibility"] = "ENABLED"
    return out
