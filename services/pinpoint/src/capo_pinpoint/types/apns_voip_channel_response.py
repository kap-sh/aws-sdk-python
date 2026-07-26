"""Generated from Smithy shape ``com.amazonaws.pinpoint#APNSVoipChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class APNSVoipChannelResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the APNs VoIP channel applies to.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the APNs VoIP channel was enabled.</p>"""
    default_authentication_method: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The default authentication method that Amazon Pinpoint uses to authenticate with APNs for this channel, key or certificate.</p>"""
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the APNs VoIP channel is enabled for the application.</p>"""
    has_credential: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>(Not used) This property is retained only for backward compatibility.</p>"""
    has_token_key: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the APNs VoIP channel is configured to communicate with APNs by using APNs tokens. To provide an authentication key for APNs tokens, set the TokenKey property of the channel.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>(Deprecated) An identifier for the APNs VoIP channel. This property is retained only for backward compatibility.</p>"""
    is_archived: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the APNs VoIP channel is archived.</p>"""
    last_modified_by: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The user who last modified the APNs VoIP channel.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the APNs VoIP channel was last modified.</p>"""
    platform: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of messaging or notification platform for the channel. For the APNs VoIP channel, this value is APNS_VOIP.</p>"""
    version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The current version of the APNs VoIP channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: APNSVoipChannelResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "default_authentication_method" in value:
        out["DefaultAuthenticationMethod"] = value["default_authentication_method"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "has_credential" in value:
        out["HasCredential"] = value["has_credential"]
    if "has_token_key" in value:
        out["HasTokenKey"] = value["has_token_key"]
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
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> APNSVoipChannelResponse:
    out: APNSVoipChannelResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "DefaultAuthenticationMethod" in data:
        out["default_authentication_method"] = data["DefaultAuthenticationMethod"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "HasCredential" in data:
        out["has_credential"] = data["HasCredential"]
    if "HasTokenKey" in data:
        out["has_token_key"] = data["HasTokenKey"]
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
    if "Version" in data:
        out["version"] = data["Version"]
    return out
