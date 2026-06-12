"""Generated from Smithy shape ``com.amazonaws.qapps#UserAppItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_arn
    import aws_sdk_qapps.types.description
    import aws_sdk_qapps.types.q_apps_timestamp
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class UserAppItem(TypedDict):
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App.</p>"""
    app_arn: "aws_sdk_qapps.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the Q App.</p>"""
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title of the Q App.</p>"""
    description: NotRequired["aws_sdk_qapps.types.description.Description"]
    """<p>The description of the Q App.</p>"""
    created_at: "aws_sdk_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time the user's association with the Q App was created.</p>"""
    can_edit: NotRequired["bool"]
    """<p>A flag indicating whether the user can edit the Q App.</p>"""
    status: NotRequired["str"]
    """<p>The status of the user's association with the Q App.</p>"""
    is_verified: "bool"
    """<p>Indicates whether the Q App has been verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAppItem) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_qapps.types.q_apps_timestamp

    out["createdAt"] = aws_sdk_qapps.types.q_apps_timestamp.serialize_json(
        value["created_at"]
    )
    if "can_edit" in value:
        out["canEdit"] = value["can_edit"]
    if "status" in value:
        out["status"] = value["status"]
    out["isVerified"] = value.get("is_verified", False)
    return out


def deserialize_json(data: dict) -> UserAppItem:
    out: UserAppItem = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("UserAppItem.app_id required")
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("UserAppItem.app_arn required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("UserAppItem.title required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["created_at"] = aws_sdk_qapps.types.q_apps_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("UserAppItem.created_at required")
    if "canEdit" in data:
        out["can_edit"] = data["canEdit"]
    if "status" in data:
        out["status"] = data["status"]
    if "isVerified" in data:
        out["is_verified"] = data["isVerified"]
    else:
        out["is_verified"] = False
    return out
