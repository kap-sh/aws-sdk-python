"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateAccountConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.account_configuration


class UpdateAccountConfigurationRequest(TypedDict, closed=True):
    account_configuration: NotRequired[
        "capo_medialive.types.account_configuration.AccountConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountConfigurationRequest) -> dict:
    out: dict = {}
    if "account_configuration" in value:
        import capo_medialive.types.account_configuration

        out["accountConfiguration"] = (
            capo_medialive.types.account_configuration.serialize_json(
                value["account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountConfigurationRequest:
    out: UpdateAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "accountConfiguration" in data:
        import capo_medialive.types.account_configuration

        out["account_configuration"] = (
            capo_medialive.types.account_configuration.deserialize_json(
                data["accountConfiguration"]
            )
        )
    return out
