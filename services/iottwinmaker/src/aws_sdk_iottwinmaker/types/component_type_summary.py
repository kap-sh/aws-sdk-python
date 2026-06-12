"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentTypeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.component_type_name
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.status
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class ComponentTypeSummary(TypedDict):
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the component type.</p>"""
    component_type_id: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component type was created.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component type was last updated.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    status: NotRequired["aws_sdk_iottwinmaker.types.status.Status"]
    """<p>The current status of the component type.</p>"""
    component_type_name: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_name.ComponentTypeName"
    ]
    """<p>The component type name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentTypeSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["componentTypeId"] = value["component_type_id"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.serialize_json(
            value["status"]
        )
    if "component_type_name" in value:
        out["componentTypeName"] = value["component_type_name"]
    return out


def deserialize_json(data: dict) -> ComponentTypeSummary:
    out: ComponentTypeSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ComponentTypeSummary.arn required")
    if "componentTypeId" in data:
        out["component_type_id"] = data["componentTypeId"]
    else:
        raise DeserializationError("ComponentTypeSummary.component_type_id required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("ComponentTypeSummary.creation_date_time required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("ComponentTypeSummary.update_date_time required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_iottwinmaker.types.status

        out["status"] = aws_sdk_iottwinmaker.types.status.deserialize_json(
            data["status"]
        )
    if "componentTypeName" in data:
        out["component_type_name"] = data["componentTypeName"]
    return out
