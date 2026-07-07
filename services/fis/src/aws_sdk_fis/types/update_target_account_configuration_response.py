"""Generated from Smithy shape ``com.amazonaws.fis#UpdateTargetAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_account_configuration


class UpdateTargetAccountConfigurationResponse(TypedDict, closed=True):
    target_account_configuration: NotRequired[
        "aws_sdk_fis.types.target_account_configuration.TargetAccountConfiguration"
    ]
    """<p>Information about the target account configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "target_account_configuration" in value:
        import aws_sdk_fis.types.target_account_configuration

        out["targetAccountConfiguration"] = (
            aws_sdk_fis.types.target_account_configuration.serialize_json(
                value["target_account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTargetAccountConfigurationResponse:
    out: UpdateTargetAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "targetAccountConfiguration" in data:
        import aws_sdk_fis.types.target_account_configuration

        out["target_account_configuration"] = (
            aws_sdk_fis.types.target_account_configuration.deserialize_json(
                data["targetAccountConfiguration"]
            )
        )
    return out
