"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceBotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_bot


class DescribeAppInstanceBotResponse(TypedDict):
    app_instance_bot: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_bot.AppInstanceBot"
    ]
    """<p>The detials of the <code>AppInstanceBot</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceBotResponse) -> dict:
    out: dict = {}
    if "app_instance_bot" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_bot

        out["AppInstanceBot"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_bot.serialize_json(
                value["app_instance_bot"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceBotResponse:
    out: DescribeAppInstanceBotResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceBot" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_bot

        out["app_instance_bot"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_bot.deserialize_json(
                data["AppInstanceBot"]
            )
        )
    return out
