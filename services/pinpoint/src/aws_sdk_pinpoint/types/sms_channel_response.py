"""Generated from Smithy shape ``com.amazonaws.pinpoint#SMSChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class SMSChannelResponse(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the SMS channel applies to.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the SMS channel was enabled.</p>"""
    enabled: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the SMS channel is enabled for the application.</p>"""
    has_credential: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>(Not used) This property is retained only for backward compatibility.</p>"""
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>(Deprecated) An identifier for the SMS channel. This property is retained only for backward compatibility.</p>"""
    is_archived: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the SMS channel is archived.</p>"""
    last_modified_by: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The user who last modified the SMS channel.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the SMS channel was last modified.</p>"""
    platform: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The type of messaging or notification platform for the channel. For the SMS channel, this value is SMS.</p>"""
    promotional_messages_per_second: NotRequired[
        "aws_sdk_pinpoint.types.__integer.__integer"
    ]
    """<p>The maximum number of promotional messages that you can send through the SMS channel each second.</p>"""
    sender_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The identity that displays on recipients' devices when they receive messages from the SMS channel.</p>"""
    short_code: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The registered short code to use when you send messages through the SMS channel.</p>"""
    transactional_messages_per_second: NotRequired[
        "aws_sdk_pinpoint.types.__integer.__integer"
    ]
    """<p>The maximum number of transactional messages that you can send through the SMS channel each second.</p>"""
    version: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The current version of the SMS channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSChannelResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "has_credential" in value:
        out["HasCredential"] = value["has_credential"]
    if "id" in value:
        out["Id"] = value["id"]
    if "is_archived" in value:
        out["IsArchived"] = value["is_archived"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "promotional_messages_per_second" in value:
        out["PromotionalMessagesPerSecond"] = value["promotional_messages_per_second"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    if "short_code" in value:
        out["ShortCode"] = value["short_code"]
    if "transactional_messages_per_second" in value:
        out["TransactionalMessagesPerSecond"] = value[
            "transactional_messages_per_second"
        ]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> SMSChannelResponse:
    out: SMSChannelResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "HasCredential" in data:
        out["has_credential"] = data["HasCredential"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "IsArchived" in data:
        out["is_archived"] = data["IsArchived"]
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    if "PromotionalMessagesPerSecond" in data:
        out["promotional_messages_per_second"] = data["PromotionalMessagesPerSecond"]
    if "SenderId" in data:
        out["sender_id"] = data["SenderId"]
    if "ShortCode" in data:
        out["short_code"] = data["ShortCode"]
    if "TransactionalMessagesPerSecond" in data:
        out["transactional_messages_per_second"] = data[
            "TransactionalMessagesPerSecond"
        ]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
