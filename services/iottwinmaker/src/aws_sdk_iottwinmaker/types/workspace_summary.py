"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#WorkspaceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.linked_services
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class WorkspaceSummary(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the workspace.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the workspace.</p>"""
    linked_services: NotRequired[
        "aws_sdk_iottwinmaker.types.linked_services.LinkedServices"
    ]
    """<p>A list of services that are linked to the workspace.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the workspace was created.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the workspace was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummary) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "linked_services" in value:
        import aws_sdk_iottwinmaker.types.linked_services

        out["linkedServices"] = (
            aws_sdk_iottwinmaker.types.linked_services.serialize_json(
                value["linked_services"]
            )
        )
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> WorkspaceSummary:
    out: WorkspaceSummary = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("WorkspaceSummary.workspace_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("WorkspaceSummary.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "linkedServices" in data:
        import aws_sdk_iottwinmaker.types.linked_services

        out["linked_services"] = (
            aws_sdk_iottwinmaker.types.linked_services.deserialize_json(
                data["linkedServices"]
            )
        )
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("WorkspaceSummary.creation_date_time required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("WorkspaceSummary.update_date_time required")
    return out
