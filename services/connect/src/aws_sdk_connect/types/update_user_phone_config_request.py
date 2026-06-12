"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserPhoneConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.user_id
    import aws_sdk_connect.types.user_phone_config


class UpdateUserPhoneConfigRequest(TypedDict):
    phone_config: "aws_sdk_connect.types.user_phone_config.UserPhoneConfig"
    """<p>Information about phone configuration settings for the user.</p>"""
    user_id: "aws_sdk_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserPhoneConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.user_phone_config

    out["PhoneConfig"] = aws_sdk_connect.types.user_phone_config.serialize_json(
        value["phone_config"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserPhoneConfigRequest:
    out: UpdateUserPhoneConfigRequest = {}  # type: ignore[typeddict-item]
    if "PhoneConfig" in data:
        import aws_sdk_connect.types.user_phone_config

        out["phone_config"] = aws_sdk_connect.types.user_phone_config.deserialize_json(
            data["PhoneConfig"]
        )
    else:
        raise DeserializationError("UpdateUserPhoneConfigRequest.phone_config required")
    return out
