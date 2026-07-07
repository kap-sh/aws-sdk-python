"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateResourceCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.update_resource_collection_action
    import aws_sdk_devops_guru.types.update_resource_collection_filter


class UpdateResourceCollectionRequest(TypedDict, closed=True):
    action: "aws_sdk_devops_guru.types.update_resource_collection_action.UpdateResourceCollectionAction"
    """<p> Specifies if the resource collection in the request is added or deleted to the resource collection. </p>"""
    resource_collection: "aws_sdk_devops_guru.types.update_resource_collection_filter.UpdateResourceCollectionFilter"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceCollectionRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.update_resource_collection_action

    out["Action"] = (
        aws_sdk_devops_guru.types.update_resource_collection_action.serialize_json(
            value["action"]
        )
    )
    import aws_sdk_devops_guru.types.update_resource_collection_filter

    out["ResourceCollection"] = (
        aws_sdk_devops_guru.types.update_resource_collection_filter.serialize_json(
            value["resource_collection"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateResourceCollectionRequest:
    out: UpdateResourceCollectionRequest = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_devops_guru.types.update_resource_collection_action

        out["action"] = (
            aws_sdk_devops_guru.types.update_resource_collection_action.deserialize_json(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("UpdateResourceCollectionRequest.action required")
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.update_resource_collection_filter

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.update_resource_collection_filter.deserialize_json(
                data["ResourceCollection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateResourceCollectionRequest.resource_collection required"
        )
    return out
