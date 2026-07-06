"""Generated from Smithy shape ``com.amazonaws.qapps#CreateQAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_definition_input
    import aws_sdk_qapps.types.description
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.tag_map
    import aws_sdk_qapps.types.title


class CreateQAppInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title of the new Q App.</p>"""
    description: NotRequired["aws_sdk_qapps.types.description.Description"]
    """<p>The description of the new Q App.</p>"""
    app_definition: "aws_sdk_qapps.types.app_definition_input.AppDefinitionInput"
    """<p>The definition of the new Q App, specifying the cards and flow.</p>"""
    tags: NotRequired["aws_sdk_qapps.types.tag_map.TagMap"]
    """<p>Optional tags to associate with the new Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQAppInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_qapps.types.app_definition_input

    out["appDefinition"] = aws_sdk_qapps.types.app_definition_input.serialize_json(
        value["app_definition"]
    )
    if "tags" in value:
        import aws_sdk_qapps.types.tag_map

        out["tags"] = aws_sdk_qapps.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateQAppInput:
    out: CreateQAppInput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateQAppInput.title required")
    if "description" in data:
        out["description"] = data["description"]
    if "appDefinition" in data:
        import aws_sdk_qapps.types.app_definition_input

        out["app_definition"] = (
            aws_sdk_qapps.types.app_definition_input.deserialize_json(
                data["appDefinition"]
            )
        )
    else:
        raise DeserializationError("CreateQAppInput.app_definition required")
    if "tags" in data:
        import aws_sdk_qapps.types.tag_map

        out["tags"] = aws_sdk_qapps.types.tag_map.deserialize_json(data["tags"])
    return out
