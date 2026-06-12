"""Generated from Smithy shape ``com.amazonaws.pinpoint#ChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class ChannelResponse(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the channel was enabled.</p>"""
    enabled: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the channel is enabled for the application.</p>"""
    has_credential: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>(Not used) This property is retained only for backward compatibility.</p>"""
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>(Deprecated) An identifier for the channel. This property is retained only for backward compatibility.</p>"""
    is_archived: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the channel is archived.</p>"""
    last_modified_by: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The user who last modified the channel.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the channel was last modified.</p>"""
    version: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The current version of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelResponse) -> dict:
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
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ChannelResponse:
    out: ChannelResponse = {}  # type: ignore[typeddict-item]
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
    if "Version" in data:
        out["version"] = data["Version"]
    return out
