"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateApplicationPortalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.sign_in_options


class UpdateApplicationPortalOptions(TypedDict, closed=True):
    sign_in_options: NotRequired["capo_sso_admin.types.sign_in_options.SignInOptions"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationPortalOptions) -> dict:
    out: dict = {}
    if "sign_in_options" in value:
        import capo_sso_admin.types.sign_in_options

        out["SignInOptions"] = (
            capo_sso_admin.types.sign_in_options.serialize_aws_json_1_1(
                value["sign_in_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationPortalOptions:
    out: UpdateApplicationPortalOptions = {}  # type: ignore[typeddict-item]
    if "SignInOptions" in data:
        import capo_sso_admin.types.sign_in_options

        out["sign_in_options"] = (
            capo_sso_admin.types.sign_in_options.deserialize_aws_json_1_1(
                data["SignInOptions"]
            )
        )
    return out
