"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateLibraryItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.app_version
    import capo_qapps.types.category_list
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.uuid


class UpdateLibraryItemOutput(TypedDict, closed=True):
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the updated library item.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App associated with the library item.</p>"""
    app_version: "capo_qapps.types.app_version.AppVersion"
    """<p>The version of the Q App associated with the library item.</p>"""
    categories: "capo_qapps.types.category_list.CategoryList"
    """<p>The categories associated with the updated library item.</p>"""
    status: "str"
    """<p>The new status of the updated library item.</p>"""
    created_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the library item was originally created.</p>"""
    created_by: "str"
    """<p>The user who originally created the library item.</p>"""
    updated_at: NotRequired["capo_qapps.types.q_apps_timestamp.QAppsTimestamp"]
    """<p>The date and time the library item was last updated.</p>"""
    updated_by: NotRequired["str"]
    """<p>The user who last updated the library item.</p>"""
    rating_count: "int"
    """<p>The number of ratings the library item has received.</p>"""
    is_rated_by_user: NotRequired["bool"]
    """<p>Whether the current user has rated the library item.</p>"""
    user_count: NotRequired["int"]
    """<p>The number of users who have the associated Q App.</p>"""
    is_verified: NotRequired["bool"]
    """<p>Indicates whether the library item has been verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLibraryItemOutput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    out["appId"] = value["app_id"]
    out["appVersion"] = value["app_version"]
    import capo_qapps.types.category_list

    out["categories"] = capo_qapps.types.category_list.serialize_json(
        value["categories"]
    )
    out["status"] = value["status"]
    import capo_qapps.types.q_apps_timestamp

    out["createdAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_qapps.types.q_apps_timestamp

        out["updatedAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["ratingCount"] = value["rating_count"]
    if "is_rated_by_user" in value:
        out["isRatedByUser"] = value["is_rated_by_user"]
    if "user_count" in value:
        out["userCount"] = value["user_count"]
    if "is_verified" in value:
        out["isVerified"] = value["is_verified"]
    return out


def deserialize_json(data: dict) -> UpdateLibraryItemOutput:
    out: UpdateLibraryItemOutput = {}  # type: ignore[typeddict-item]
    if "libraryItemId" in data:
        out["library_item_id"] = data["libraryItemId"]
    else:
        raise DeserializationError("UpdateLibraryItemOutput.library_item_id required")
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("UpdateLibraryItemOutput.app_id required")
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("UpdateLibraryItemOutput.app_version required")
    if "categories" in data:
        import capo_qapps.types.category_list

        out["categories"] = capo_qapps.types.category_list.deserialize_json(
            data["categories"]
        )
    else:
        raise DeserializationError("UpdateLibraryItemOutput.categories required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("UpdateLibraryItemOutput.status required")
    if "createdAt" in data:
        import capo_qapps.types.q_apps_timestamp

        out["created_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("UpdateLibraryItemOutput.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("UpdateLibraryItemOutput.created_by required")
    if "updatedAt" in data:
        import capo_qapps.types.q_apps_timestamp

        out["updated_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "ratingCount" in data:
        out["rating_count"] = data["ratingCount"]
    else:
        raise DeserializationError("UpdateLibraryItemOutput.rating_count required")
    if "isRatedByUser" in data:
        out["is_rated_by_user"] = data["isRatedByUser"]
    if "userCount" in data:
        out["user_count"] = data["userCount"]
    if "isVerified" in data:
        out["is_verified"] = data["isVerified"]
    return out
