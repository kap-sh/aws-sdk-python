"""Generated from Smithy shape ``com.amazonaws.qapps#CreateLibraryItemOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.q_apps_timestamp
    import aws_sdk_qapps.types.uuid


class CreateLibraryItemOutput(TypedDict):
    library_item_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the new library item.</p>"""
    status: "str"
    r"""<p>The status of the new library item, such as \"Published\".</p>"""
    created_at: "aws_sdk_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the library item was created.</p>"""
    created_by: "str"
    """<p>The user who created the library item.</p>"""
    updated_at: NotRequired["aws_sdk_qapps.types.q_apps_timestamp.QAppsTimestamp"]
    """<p>The date and time the library item was last updated.</p>"""
    updated_by: NotRequired["str"]
    """<p>The user who last updated the library item.</p>"""
    rating_count: "int"
    """<p>The number of ratings the library item has received from users.</p>"""
    is_verified: NotRequired["bool"]
    """<p>Indicates whether the library item has been verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLibraryItemOutput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    out["status"] = value["status"]
    import aws_sdk_qapps.types.q_apps_timestamp

    out["createdAt"] = aws_sdk_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["updatedAt"] = aws_sdk_qapps.types.q_apps_timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["ratingCount"] = value["rating_count"]
    if "is_verified" in value:
        out["isVerified"] = value["is_verified"]
    return out


def deserialize_json(data: dict) -> CreateLibraryItemOutput:
    out: CreateLibraryItemOutput = {}  # type: ignore[typeddict-item]
    if "libraryItemId" in data:
        out["library_item_id"] = data["libraryItemId"]
    else:
        raise DeserializationError("CreateLibraryItemOutput.library_item_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("CreateLibraryItemOutput.status required")
    if "createdAt" in data:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["created_at"] = aws_sdk_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateLibraryItemOutput.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateLibraryItemOutput.created_by required")
    if "updatedAt" in data:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["updated_at"] = aws_sdk_qapps.types.q_apps_timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "ratingCount" in data:
        out["rating_count"] = data["ratingCount"]
    else:
        raise DeserializationError("CreateLibraryItemOutput.rating_count required")
    if "isVerified" in data:
        out["is_verified"] = data["isVerified"]
    return out
