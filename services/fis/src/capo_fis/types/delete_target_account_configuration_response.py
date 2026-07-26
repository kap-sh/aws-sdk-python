"""Generated from Smithy shape ``com.amazonaws.fis#DeleteTargetAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.target_account_configuration


class DeleteTargetAccountConfigurationResponse(TypedDict, closed=True):
    target_account_configuration: NotRequired[
        "capo_fis.types.target_account_configuration.TargetAccountConfiguration"
    ]
    """<p>Information about the target account configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "target_account_configuration" in value:
        import capo_fis.types.target_account_configuration

        out["targetAccountConfiguration"] = (
            capo_fis.types.target_account_configuration.serialize_json(
                value["target_account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteTargetAccountConfigurationResponse:
    out: DeleteTargetAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "targetAccountConfiguration" in data:
        import capo_fis.types.target_account_configuration

        out["target_account_configuration"] = (
            capo_fis.types.target_account_configuration.deserialize_json(
                data["targetAccountConfiguration"]
            )
        )
    return out
