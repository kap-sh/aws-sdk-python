"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdateApplicationPortalOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.sign_in_options


class UpdateApplicationPortalOptions(TypedDict):
    sign_in_options: NotRequired[
        "aws_sdk_sso_admin.types.sign_in_options.SignInOptions"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationPortalOptions) -> dict:
    out: dict = {}
    if "sign_in_options" in value:
        import aws_sdk_sso_admin.types.sign_in_options

        out["SignInOptions"] = (
            aws_sdk_sso_admin.types.sign_in_options.serialize_aws_json_1_1(
                value["sign_in_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationPortalOptions:
    out: UpdateApplicationPortalOptions = {}  # type: ignore[typeddict-item]
    if "SignInOptions" in data:
        import aws_sdk_sso_admin.types.sign_in_options

        out["sign_in_options"] = (
            aws_sdk_sso_admin.types.sign_in_options.deserialize_aws_json_1_1(
                data["SignInOptions"]
            )
        )
    return out
