"""Generated from Smithy shape ``com.amazonaws.backupsearch#StartSearchJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backupsearch.types.encryption_key_arn
    import capo_backupsearch.types.item_filters
    import capo_backupsearch.types.search_scope
    import capo_backupsearch.types.tag_map


class StartSearchJobInput(TypedDict, closed=True):
    tags: NotRequired["capo_backupsearch.types.tag_map.TagMap"]
    """<p>List of tags returned by the operation.</p>"""
    name: NotRequired["str"]
    """<p>Include alphanumeric characters to create a name for this search job.</p>"""
    encryption_key_arn: NotRequired[
        "capo_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The encryption key for the specified search job.</p>"""
    client_token: NotRequired["str"]
    """<p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>"""
    search_scope: "capo_backupsearch.types.search_scope.SearchScope"
    """<p>This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.</p>"""
    item_filters: NotRequired["capo_backupsearch.types.item_filters.ItemFilters"]
    """<p>Item Filters represent all input item properties specified when the search was created.</p> <p>Contains either EBSItemFilters or S3ItemFilters</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSearchJobInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_backupsearch.types.tag_map

        out["Tags"] = capo_backupsearch.types.tag_map.serialize_json(value["tags"])
    if "name" in value:
        out["Name"] = value["name"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_backupsearch.types.search_scope

    out["SearchScope"] = capo_backupsearch.types.search_scope.serialize_json(
        value["search_scope"]
    )
    if "item_filters" in value:
        import capo_backupsearch.types.item_filters

        out["ItemFilters"] = capo_backupsearch.types.item_filters.serialize_json(
            value["item_filters"]
        )
    return out


def deserialize_json(data: dict) -> StartSearchJobInput:
    out: StartSearchJobInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_backupsearch.types.tag_map

        out["tags"] = capo_backupsearch.types.tag_map.deserialize_json(data["Tags"])
    if "Name" in data:
        out["name"] = data["Name"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "SearchScope" in data:
        import capo_backupsearch.types.search_scope

        out["search_scope"] = capo_backupsearch.types.search_scope.deserialize_json(
            data["SearchScope"]
        )
    else:
        raise DeserializationError("StartSearchJobInput.search_scope required")
    if "ItemFilters" in data:
        import capo_backupsearch.types.item_filters

        out["item_filters"] = capo_backupsearch.types.item_filters.deserialize_json(
            data["ItemFilters"]
        )
    return out
