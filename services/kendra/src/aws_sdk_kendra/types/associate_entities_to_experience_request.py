"""Generated from Smithy shape ``com.amazonaws.kendra#AssociateEntitiesToExperienceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.associate_entity_list
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.index_id


class AssociateEntitiesToExperienceRequest(TypedDict):
    id: "aws_sdk_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    entity_list: "aws_sdk_kendra.types.associate_entity_list.AssociateEntityList"
    """<p>Lists users or groups in your IAM Identity Center identity source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateEntitiesToExperienceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    import aws_sdk_kendra.types.associate_entity_list

    out["EntityList"] = (
        aws_sdk_kendra.types.associate_entity_list.serialize_aws_json_1_1(
            value["entity_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateEntitiesToExperienceRequest:
    out: AssociateEntitiesToExperienceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("AssociateEntitiesToExperienceRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "AssociateEntitiesToExperienceRequest.index_id required"
        )
    if "EntityList" in data:
        import aws_sdk_kendra.types.associate_entity_list

        out["entity_list"] = (
            aws_sdk_kendra.types.associate_entity_list.deserialize_aws_json_1_1(
                data["EntityList"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateEntitiesToExperienceRequest.entity_list required"
        )
    return out
