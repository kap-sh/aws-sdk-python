"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApplicationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.write_application_settings_request


class UpdateApplicationSettingsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    write_application_settings_request: NotRequired[
        "aws_sdk_pinpoint.types.write_application_settings_request.WriteApplicationSettingsRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationSettingsRequest) -> dict:
    out: dict = {}
    if "write_application_settings_request" in value:
        import aws_sdk_pinpoint.types.write_application_settings_request

        out["WriteApplicationSettingsRequest"] = (
            aws_sdk_pinpoint.types.write_application_settings_request.serialize_json(
                value["write_application_settings_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationSettingsRequest:
    out: UpdateApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
    if "WriteApplicationSettingsRequest" in data:
        import aws_sdk_pinpoint.types.write_application_settings_request

        out["write_application_settings_request"] = (
            aws_sdk_pinpoint.types.write_application_settings_request.deserialize_json(
                data["WriteApplicationSettingsRequest"]
            )
        )
    return out
