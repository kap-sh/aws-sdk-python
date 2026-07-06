"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_definition_input
    import aws_sdk_qapps.types.description
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class UpdateQAppInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to update.</p>"""
    title: NotRequired["aws_sdk_qapps.types.title.Title"]
    """<p>The new title for the Q App.</p>"""
    description: NotRequired["aws_sdk_qapps.types.description.Description"]
    """<p>The new description for the Q App.</p>"""
    app_definition: NotRequired[
        "aws_sdk_qapps.types.app_definition_input.AppDefinitionInput"
    ]
    """<p>The new definition specifying the cards and flow for the Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "app_definition" in value:
        import aws_sdk_qapps.types.app_definition_input

        out["appDefinition"] = aws_sdk_qapps.types.app_definition_input.serialize_json(
            value["app_definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppInput:
    out: UpdateQAppInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("UpdateQAppInput.app_id required")
    if "title" in data:
        out["title"] = data["title"]
    if "description" in data:
        out["description"] = data["description"]
    if "appDefinition" in data:
        import aws_sdk_qapps.types.app_definition_input

        out["app_definition"] = (
            aws_sdk_qapps.types.app_definition_input.deserialize_json(
                data["appDefinition"]
            )
        )
    return out
