"""Generated from Smithy shape ``com.amazonaws.qapps#CreateLibraryItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_version
    import aws_sdk_qapps.types.category_id_list
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class CreateLibraryItemInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Amazon Q App to publish to the library.</p>"""
    app_version: "aws_sdk_qapps.types.app_version.AppVersion"
    """<p>The version of the Amazon Q App to publish to the library.</p>"""
    categories: "aws_sdk_qapps.types.category_id_list.CategoryIdList"
    """<p>The categories to associate with the library item for easier discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLibraryItemInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appVersion"] = value["app_version"]
    import aws_sdk_qapps.types.category_id_list

    out["categories"] = aws_sdk_qapps.types.category_id_list.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> CreateLibraryItemInput:
    out: CreateLibraryItemInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("CreateLibraryItemInput.app_id required")
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("CreateLibraryItemInput.app_version required")
    if "categories" in data:
        import aws_sdk_qapps.types.category_id_list

        out["categories"] = aws_sdk_qapps.types.category_id_list.deserialize_json(
            data["categories"]
        )
    else:
        raise DeserializationError("CreateLibraryItemInput.categories required")
    return out
