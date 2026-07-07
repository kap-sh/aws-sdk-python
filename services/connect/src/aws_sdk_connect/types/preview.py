"""Generated from Smithy shape ``com.amazonaws.connect#Preview``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.allowed_user_actions
    import aws_sdk_connect.types.post_accept_timeout_config


class Preview(TypedDict, closed=True):
    post_accept_timeout_config: (
        "aws_sdk_connect.types.post_accept_timeout_config.PostAcceptTimeoutConfig"
    )
    """<p>Countdown timer configuration after the agent accepted the preview outbound contact.</p>"""
    allowed_user_actions: (
        "aws_sdk_connect.types.allowed_user_actions.AllowedUserActions"
    )
    """<p>The actions the agent can perform after accepting the preview outbound contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Preview) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.post_accept_timeout_config

    out["PostAcceptTimeoutConfig"] = (
        aws_sdk_connect.types.post_accept_timeout_config.serialize_json(
            value["post_accept_timeout_config"]
        )
    )
    import aws_sdk_connect.types.allowed_user_actions

    out["AllowedUserActions"] = (
        aws_sdk_connect.types.allowed_user_actions.serialize_json(
            value["allowed_user_actions"]
        )
    )
    return out


def deserialize_json(data: dict) -> Preview:
    out: Preview = {}  # type: ignore[typeddict-item]
    if "PostAcceptTimeoutConfig" in data:
        import aws_sdk_connect.types.post_accept_timeout_config

        out["post_accept_timeout_config"] = (
            aws_sdk_connect.types.post_accept_timeout_config.deserialize_json(
                data["PostAcceptTimeoutConfig"]
            )
        )
    else:
        raise DeserializationError("Preview.post_accept_timeout_config required")
    if "AllowedUserActions" in data:
        import aws_sdk_connect.types.allowed_user_actions

        out["allowed_user_actions"] = (
            aws_sdk_connect.types.allowed_user_actions.deserialize_json(
                data["AllowedUserActions"]
            )
        )
    else:
        raise DeserializationError("Preview.allowed_user_actions required")
    return out
