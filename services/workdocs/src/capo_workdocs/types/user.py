"""Generated from Smithy shape ``com.amazonaws.workdocs#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.email_address_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.locale_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.time_zone_id_type
    import capo_workdocs.types.timestamp_type
    import capo_workdocs.types.user_attribute_value_type
    import capo_workdocs.types.user_status_type
    import capo_workdocs.types.user_storage_metadata
    import capo_workdocs.types.user_type
    import capo_workdocs.types.username_type


class User(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user.</p>"""
    username: NotRequired["capo_workdocs.types.username_type.UsernameType"]
    """<p>The login name of the user.</p>"""
    email_address: NotRequired[
        "capo_workdocs.types.email_address_type.EmailAddressType"
    ]
    """<p>The email address of the user.</p>"""
    given_name: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The given name of the user.</p>"""
    surname: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The surname of the user.</p>"""
    organization_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    root_folder_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the root folder.</p>"""
    recycle_bin_folder_id: NotRequired[
        "capo_workdocs.types.resource_id_type.ResourceIdType"
    ]
    """<p>The ID of the recycle bin folder.</p>"""
    status: NotRequired["capo_workdocs.types.user_status_type.UserStatusType"]
    """<p>The status of the user.</p>"""
    type: NotRequired["capo_workdocs.types.user_type.UserType"]
    """<p>The type of user.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the user was created.</p>"""
    modified_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the user was modified.</p>"""
    time_zone_id: NotRequired["capo_workdocs.types.time_zone_id_type.TimeZoneIdType"]
    """<p>The time zone ID of the user.</p>"""
    locale: NotRequired["capo_workdocs.types.locale_type.LocaleType"]
    """<p>The locale of the user.</p>"""
    storage: NotRequired[
        "capo_workdocs.types.user_storage_metadata.UserStorageMetadata"
    ]
    """<p>The storage for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "username" in value:
        out["Username"] = value["username"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "root_folder_id" in value:
        out["RootFolderId"] = value["root_folder_id"]
    if "recycle_bin_folder_id" in value:
        out["RecycleBinFolderId"] = value["recycle_bin_folder_id"]
    if "status" in value:
        import capo_workdocs.types.user_status_type

        out["Status"] = capo_workdocs.types.user_status_type.serialize_json(
            value["status"]
        )
    if "type" in value:
        import capo_workdocs.types.user_type

        out["Type"] = capo_workdocs.types.user_type.serialize_json(value["type"])
    if "created_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "modified_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["ModifiedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["modified_timestamp"]
        )
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "locale" in value:
        import capo_workdocs.types.locale_type

        out["Locale"] = capo_workdocs.types.locale_type.serialize_json(value["locale"])
    if "storage" in value:
        import capo_workdocs.types.user_storage_metadata

        out["Storage"] = capo_workdocs.types.user_storage_metadata.serialize_json(
            value["storage"]
        )
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "RootFolderId" in data:
        out["root_folder_id"] = data["RootFolderId"]
    if "RecycleBinFolderId" in data:
        out["recycle_bin_folder_id"] = data["RecycleBinFolderId"]
    if "Status" in data:
        import capo_workdocs.types.user_status_type

        out["status"] = capo_workdocs.types.user_status_type.deserialize_json(
            data["Status"]
        )
    if "Type" in data:
        import capo_workdocs.types.user_type

        out["type"] = capo_workdocs.types.user_type.deserialize_json(data["Type"])
    if "CreatedTimestamp" in data:
        import capo_workdocs.types.timestamp_type

        out["created_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "ModifiedTimestamp" in data:
        import capo_workdocs.types.timestamp_type

        out["modified_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["ModifiedTimestamp"]
        )
    if "TimeZoneId" in data:
        out["time_zone_id"] = data["TimeZoneId"]
    if "Locale" in data:
        import capo_workdocs.types.locale_type

        out["locale"] = capo_workdocs.types.locale_type.deserialize_json(data["Locale"])
    if "Storage" in data:
        import capo_workdocs.types.user_storage_metadata

        out["storage"] = capo_workdocs.types.user_storage_metadata.deserialize_json(
            data["Storage"]
        )
    return out
