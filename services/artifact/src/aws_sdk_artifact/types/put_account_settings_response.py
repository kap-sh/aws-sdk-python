"""Generated from Smithy shape ``com.amazonaws.artifact#PutAccountSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_artifact.types.account_settings


class PutAccountSettingsResponse(TypedDict):
    account_settings: NotRequired[
        "aws_sdk_artifact.types.account_settings.AccountSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import aws_sdk_artifact.types.account_settings

        out["accountSettings"] = aws_sdk_artifact.types.account_settings.serialize_json(
            value["account_settings"]
        )
    return out


def deserialize_json(data: dict) -> PutAccountSettingsResponse:
    out: PutAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "accountSettings" in data:
        import aws_sdk_artifact.types.account_settings

        out["account_settings"] = (
            aws_sdk_artifact.types.account_settings.deserialize_json(
                data["accountSettings"]
            )
        )
    return out
