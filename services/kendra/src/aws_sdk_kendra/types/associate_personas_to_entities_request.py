"""Generated from Smithy shape ``com.amazonaws.kendra#AssociatePersonasToEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_persona_configuration_list
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.index_id


class AssociatePersonasToEntitiesRequest(TypedDict):
    id: "aws_sdk_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    personas: "aws_sdk_kendra.types.entity_persona_configuration_list.EntityPersonaConfigurationList"
    r"""<p>The personas that define the specific permissions of users or groups in your IAM Identity Center identity source. The available personas or access roles are <code>Owner</code> and <code>Viewer</code>. For more information on these personas, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html#access-search-experience\">Providing access to your search page</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatePersonasToEntitiesRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    import aws_sdk_kendra.types.entity_persona_configuration_list

    out["Personas"] = (
        aws_sdk_kendra.types.entity_persona_configuration_list.serialize_aws_json_1_1(
            value["personas"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatePersonasToEntitiesRequest:
    out: AssociatePersonasToEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("AssociatePersonasToEntitiesRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "AssociatePersonasToEntitiesRequest.index_id required"
        )
    if "Personas" in data:
        import aws_sdk_kendra.types.entity_persona_configuration_list

        out["personas"] = (
            aws_sdk_kendra.types.entity_persona_configuration_list.deserialize_aws_json_1_1(
                data["Personas"]
            )
        )
    else:
        raise DeserializationError(
            "AssociatePersonasToEntitiesRequest.personas required"
        )
    return out
