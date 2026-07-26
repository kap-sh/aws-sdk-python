"""Generated from Smithy shape ``com.amazonaws.kendra#AssociateEntitiesToExperienceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.associate_entities_to_experience_failed_entity_list


class AssociateEntitiesToExperienceResponse(TypedDict, closed=True):
    failed_entity_list: NotRequired[
        "capo_kendra.types.associate_entities_to_experience_failed_entity_list.AssociateEntitiesToExperienceFailedEntityList"
    ]
    """<p>Lists the users or groups in your IAM Identity Center identity source that failed to properly configure with your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateEntitiesToExperienceResponse) -> dict:
    out: dict = {}
    if "failed_entity_list" in value:
        import capo_kendra.types.associate_entities_to_experience_failed_entity_list

        out["FailedEntityList"] = (
            capo_kendra.types.associate_entities_to_experience_failed_entity_list.serialize_aws_json_1_1(
                value["failed_entity_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateEntitiesToExperienceResponse:
    out: AssociateEntitiesToExperienceResponse = {}  # type: ignore[typeddict-item]
    if "FailedEntityList" in data:
        import capo_kendra.types.associate_entities_to_experience_failed_entity_list

        out["failed_entity_list"] = (
            capo_kendra.types.associate_entities_to_experience_failed_entity_list.deserialize_aws_json_1_1(
                data["FailedEntityList"]
            )
        )
    return out
