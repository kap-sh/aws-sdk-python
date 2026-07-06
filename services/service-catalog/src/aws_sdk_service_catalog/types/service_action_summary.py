"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.service_action_definition_type
    import aws_sdk_service_catalog.types.service_action_description
    import aws_sdk_service_catalog.types.service_action_name


class ServiceActionSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The self-service action identifier.</p>"""
    name: NotRequired[
        "aws_sdk_service_catalog.types.service_action_name.ServiceActionName"
    ]
    """<p>The self-service action name.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.service_action_description.ServiceActionDescription"
    ]
    """<p>The self-service action description.</p>"""
    definition_type: NotRequired[
        "aws_sdk_service_catalog.types.service_action_definition_type.ServiceActionDefinitionType"
    ]
    """<p>The self-service action definition type. For example, <code>SSM_AUTOMATION</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "definition_type" in value:
        import aws_sdk_service_catalog.types.service_action_definition_type

        out["DefinitionType"] = (
            aws_sdk_service_catalog.types.service_action_definition_type.serialize_aws_json_1_1(
                value["definition_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceActionSummary:
    out: ServiceActionSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DefinitionType" in data:
        import aws_sdk_service_catalog.types.service_action_definition_type

        out["definition_type"] = (
            aws_sdk_service_catalog.types.service_action_definition_type.deserialize_aws_json_1_1(
                data["DefinitionType"]
            )
        )
    return out
