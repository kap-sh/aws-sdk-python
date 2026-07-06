"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApplicationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.application_settings_resource


class GetApplicationSettingsResponse(TypedDict, closed=True):
    application_settings_resource: NotRequired[
        "aws_sdk_pinpoint.types.application_settings_resource.ApplicationSettingsResource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationSettingsResponse) -> dict:
    out: dict = {}
    if "application_settings_resource" in value:
        import aws_sdk_pinpoint.types.application_settings_resource

        out["ApplicationSettingsResource"] = (
            aws_sdk_pinpoint.types.application_settings_resource.serialize_json(
                value["application_settings_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationSettingsResponse:
    out: GetApplicationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationSettingsResource" in data:
        import aws_sdk_pinpoint.types.application_settings_resource

        out["application_settings_resource"] = (
            aws_sdk_pinpoint.types.application_settings_resource.deserialize_json(
                data["ApplicationSettingsResource"]
            )
        )
    return out
