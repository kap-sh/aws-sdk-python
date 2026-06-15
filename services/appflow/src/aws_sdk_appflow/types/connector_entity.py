"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.label
    import aws_sdk_appflow.types.name


class ConnectorEntity(TypedDict):
    name: "aws_sdk_appflow.types.name.Name"
    """<p> The name of the connector entity. </p>"""
    label: NotRequired["aws_sdk_appflow.types.label.Label"]
    """<p> The label applied to the connector entity. </p>"""
    has_nested_entities: "aws_sdk_appflow.types.boolean.Boolean"
    r"""<p> Specifies whether the connector entity is a parent or a category and has more entities nested underneath it. If another call is made with <code>entitiesPath = \"the_current_entity_name_with_hasNestedEntities_true\"</code>, then it returns the nested entities underneath it. This provides a way to retrieve all supported entities in a recursive fashion. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEntity) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "label" in value:
        out["label"] = value["label"]
    out["hasNestedEntities"] = value.get("has_nested_entities", False)
    return out


def deserialize_json(data: dict) -> ConnectorEntity:
    out: ConnectorEntity = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConnectorEntity.name required")
    if "label" in data:
        out["label"] = data["label"]
    if "hasNestedEntities" in data:
        out["has_nested_entities"] = data["hasNestedEntities"]
    else:
        out["has_nested_entities"] = False
    return out
