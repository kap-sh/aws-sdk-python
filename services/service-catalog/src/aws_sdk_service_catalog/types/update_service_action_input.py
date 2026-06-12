"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateServiceActionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.service_action_definition_map
    import aws_sdk_service_catalog.types.service_action_description
    import aws_sdk_service_catalog.types.service_action_name


class UpdateServiceActionInput(TypedDict):
    id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier.</p>"""
    name: NotRequired[
        "aws_sdk_service_catalog.types.service_action_name.ServiceActionName"
    ]
    """<p>The self-service action name.</p>"""
    definition: NotRequired[
        "aws_sdk_service_catalog.types.service_action_definition_map.ServiceActionDefinitionMap"
    ]
    """<p>A map that defines the self-service action.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.service_action_description.ServiceActionDescription"
    ]
    """<p>The self-service action description.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceActionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "definition" in value:
        import aws_sdk_service_catalog.types.service_action_definition_map

        out["Definition"] = (
            aws_sdk_service_catalog.types.service_action_definition_map.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceActionInput:
    out: UpdateServiceActionInput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateServiceActionInput.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Definition" in data:
        import aws_sdk_service_catalog.types.service_action_definition_map

        out["definition"] = (
            aws_sdk_service_catalog.types.service_action_definition_map.deserialize_aws_json_1_1(
                data["Definition"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    return out
