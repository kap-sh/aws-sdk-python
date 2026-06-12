"""Generated from Smithy shape ``com.amazonaws.kendra#DisassociatePersonasFromEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_ids_list
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.index_id


class DisassociatePersonasFromEntitiesRequest(TypedDict):
    id: "aws_sdk_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    entity_ids: "aws_sdk_kendra.types.entity_ids_list.EntityIdsList"
    """<p>The identifiers of users or groups in your IAM Identity Center identity source. For example, user IDs could be user emails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociatePersonasFromEntitiesRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    import aws_sdk_kendra.types.entity_ids_list

    out["EntityIds"] = aws_sdk_kendra.types.entity_ids_list.serialize_aws_json_1_1(
        value["entity_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociatePersonasFromEntitiesRequest:
    out: DisassociatePersonasFromEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "DisassociatePersonasFromEntitiesRequest.id required"
        )
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "DisassociatePersonasFromEntitiesRequest.index_id required"
        )
    if "EntityIds" in data:
        import aws_sdk_kendra.types.entity_ids_list

        out["entity_ids"] = (
            aws_sdk_kendra.types.entity_ids_list.deserialize_aws_json_1_1(
                data["EntityIds"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociatePersonasFromEntitiesRequest.entity_ids required"
        )
    return out
