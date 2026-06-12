"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.in_app_message_body_config
    import aws_sdk_pinpoint.types.in_app_message_button
    import aws_sdk_pinpoint.types.in_app_message_header_config


class InAppMessageContent(TypedDict):
    background_color: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The background color for the message.</p>"""
    body_config: NotRequired[
        "aws_sdk_pinpoint.types.in_app_message_body_config.InAppMessageBodyConfig"
    ]
    """<p>The configuration for the message body.</p>"""
    header_config: NotRequired[
        "aws_sdk_pinpoint.types.in_app_message_header_config.InAppMessageHeaderConfig"
    ]
    """<p>The configuration for the message header.</p>"""
    image_url: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The image url for the background of message.</p>"""
    primary_btn: NotRequired[
        "aws_sdk_pinpoint.types.in_app_message_button.InAppMessageButton"
    ]
    """<p>The first button inside the message.</p>"""
    secondary_btn: NotRequired[
        "aws_sdk_pinpoint.types.in_app_message_button.InAppMessageButton"
    ]
    """<p>The second button inside message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageContent) -> dict:
    out: dict = {}
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    if "body_config" in value:
        import aws_sdk_pinpoint.types.in_app_message_body_config

        out["BodyConfig"] = (
            aws_sdk_pinpoint.types.in_app_message_body_config.serialize_json(
                value["body_config"]
            )
        )
    if "header_config" in value:
        import aws_sdk_pinpoint.types.in_app_message_header_config

        out["HeaderConfig"] = (
            aws_sdk_pinpoint.types.in_app_message_header_config.serialize_json(
                value["header_config"]
            )
        )
    if "image_url" in value:
        out["ImageUrl"] = value["image_url"]
    if "primary_btn" in value:
        import aws_sdk_pinpoint.types.in_app_message_button

        out["PrimaryBtn"] = aws_sdk_pinpoint.types.in_app_message_button.serialize_json(
            value["primary_btn"]
        )
    if "secondary_btn" in value:
        import aws_sdk_pinpoint.types.in_app_message_button

        out["SecondaryBtn"] = (
            aws_sdk_pinpoint.types.in_app_message_button.serialize_json(
                value["secondary_btn"]
            )
        )
    return out


def deserialize_json(data: dict) -> InAppMessageContent:
    out: InAppMessageContent = {}  # type: ignore[typeddict-item]
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    if "BodyConfig" in data:
        import aws_sdk_pinpoint.types.in_app_message_body_config

        out["body_config"] = (
            aws_sdk_pinpoint.types.in_app_message_body_config.deserialize_json(
                data["BodyConfig"]
            )
        )
    if "HeaderConfig" in data:
        import aws_sdk_pinpoint.types.in_app_message_header_config

        out["header_config"] = (
            aws_sdk_pinpoint.types.in_app_message_header_config.deserialize_json(
                data["HeaderConfig"]
            )
        )
    if "ImageUrl" in data:
        out["image_url"] = data["ImageUrl"]
    if "PrimaryBtn" in data:
        import aws_sdk_pinpoint.types.in_app_message_button

        out["primary_btn"] = (
            aws_sdk_pinpoint.types.in_app_message_button.deserialize_json(
                data["PrimaryBtn"]
            )
        )
    if "SecondaryBtn" in data:
        import aws_sdk_pinpoint.types.in_app_message_button

        out["secondary_btn"] = (
            aws_sdk_pinpoint.types.in_app_message_button.deserialize_json(
                data["SecondaryBtn"]
            )
        )
    return out
