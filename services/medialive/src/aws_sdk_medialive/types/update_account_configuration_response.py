"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateAccountConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.account_configuration


class UpdateAccountConfigurationResponse(TypedDict):
    account_configuration: NotRequired[
        "aws_sdk_medialive.types.account_configuration.AccountConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "account_configuration" in value:
        import aws_sdk_medialive.types.account_configuration

        out["accountConfiguration"] = (
            aws_sdk_medialive.types.account_configuration.serialize_json(
                value["account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountConfigurationResponse:
    out: UpdateAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "accountConfiguration" in data:
        import aws_sdk_medialive.types.account_configuration

        out["account_configuration"] = (
            aws_sdk_medialive.types.account_configuration.deserialize_json(
                data["accountConfiguration"]
            )
        )
    return out
