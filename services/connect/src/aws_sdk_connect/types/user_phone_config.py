"""Generated from Smithy shape ``com.amazonaws.connect#UserPhoneConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.after_contact_work_time_limit
    import aws_sdk_connect.types.auto_accept
    import aws_sdk_connect.types.persistent_connection
    import aws_sdk_connect.types.phone_type
    import aws_sdk_connect.types.sensitive_phone_number


class UserPhoneConfig(TypedDict, closed=True):
    phone_type: "aws_sdk_connect.types.phone_type.PhoneType"
    """<p>The phone type.</p>"""
    auto_accept: "aws_sdk_connect.types.auto_accept.AutoAccept"
    """<p>The Auto accept setting.</p>"""
    after_contact_work_time_limit: (
        "aws_sdk_connect.types.after_contact_work_time_limit.AfterContactWorkTimeLimit"
    )
    """<p>The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you don't want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW. </p> <note> <p>When returned by a <code>SearchUsers</code> call, <code>AfterContactWorkTimeLimit</code> is returned in milliseconds. </p> </note>"""
    desk_phone_number: NotRequired[
        "aws_sdk_connect.types.sensitive_phone_number.SensitivePhoneNumber"
    ]
    """<p>The phone number for the user's desk phone.</p>"""
    persistent_connection: NotRequired[
        "aws_sdk_connect.types.persistent_connection.PersistentConnection"
    ]
    """<p>The persistent connection setting for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPhoneConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.phone_type

    out["PhoneType"] = aws_sdk_connect.types.phone_type.serialize_json(
        value.get("phone_type", "SOFT_PHONE")
    )
    out["AutoAccept"] = value.get("auto_accept", False)
    out["AfterContactWorkTimeLimit"] = value.get("after_contact_work_time_limit", 0)
    if "desk_phone_number" in value:
        out["DeskPhoneNumber"] = value["desk_phone_number"]
    if "persistent_connection" in value:
        out["PersistentConnection"] = value["persistent_connection"]
    return out


def deserialize_json(data: dict) -> UserPhoneConfig:
    out: UserPhoneConfig = {}  # type: ignore[typeddict-item]
    if "PhoneType" in data:
        import aws_sdk_connect.types.phone_type

        out["phone_type"] = aws_sdk_connect.types.phone_type.deserialize_json(
            data["PhoneType"]
        )
    else:
        out["phone_type"] = "SOFT_PHONE"
    if "AutoAccept" in data:
        out["auto_accept"] = data["AutoAccept"]
    else:
        out["auto_accept"] = False
    if "AfterContactWorkTimeLimit" in data:
        out["after_contact_work_time_limit"] = data["AfterContactWorkTimeLimit"]
    else:
        out["after_contact_work_time_limit"] = 0
    if "DeskPhoneNumber" in data:
        out["desk_phone_number"] = data["DeskPhoneNumber"]
    if "PersistentConnection" in data:
        out["persistent_connection"] = data["PersistentConnection"]
    return out
