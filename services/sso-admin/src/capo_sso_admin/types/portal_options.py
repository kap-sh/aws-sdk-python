"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PortalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_visibility
    import capo_sso_admin.types.sign_in_options


class PortalOptions(TypedDict, closed=True):
    sign_in_options: NotRequired["capo_sso_admin.types.sign_in_options.SignInOptions"]
    """<p>A structure that describes the sign-in options for the access portal.</p>"""
    visibility: "capo_sso_admin.types.application_visibility.ApplicationVisibility"
    """<p>Indicates whether this application is visible in the access portal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortalOptions) -> dict:
    out: dict = {}
    if "sign_in_options" in value:
        import capo_sso_admin.types.sign_in_options

        out["SignInOptions"] = (
            capo_sso_admin.types.sign_in_options.serialize_aws_json_1_1(
                value["sign_in_options"]
            )
        )
    import capo_sso_admin.types.application_visibility

    out["Visibility"] = (
        capo_sso_admin.types.application_visibility.serialize_aws_json_1_1(
            value.get("visibility", "ENABLED")
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PortalOptions:
    out: PortalOptions = {}  # type: ignore[typeddict-item]
    if "SignInOptions" in data:
        import capo_sso_admin.types.sign_in_options

        out["sign_in_options"] = (
            capo_sso_admin.types.sign_in_options.deserialize_aws_json_1_1(
                data["SignInOptions"]
            )
        )
    if "Visibility" in data:
        import capo_sso_admin.types.application_visibility

        out["visibility"] = (
            capo_sso_admin.types.application_visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    else:
        out["visibility"] = "ENABLED"
    return out
