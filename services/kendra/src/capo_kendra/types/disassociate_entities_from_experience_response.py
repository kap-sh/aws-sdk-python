"""Generated from Smithy shape ``com.amazonaws.kendra#DisassociateEntitiesFromExperienceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.failed_entity_list


class DisassociateEntitiesFromExperienceResponse(TypedDict, closed=True):
    failed_entity_list: NotRequired[
        "capo_kendra.types.failed_entity_list.FailedEntityList"
    ]
    """<p>Lists the users or groups in your IAM Identity Center identity source that failed to properly remove access to your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateEntitiesFromExperienceResponse) -> dict:
    out: dict = {}
    if "failed_entity_list" in value:
        import capo_kendra.types.failed_entity_list

        out["FailedEntityList"] = (
            capo_kendra.types.failed_entity_list.serialize_aws_json_1_1(
                value["failed_entity_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateEntitiesFromExperienceResponse:
    out: DisassociateEntitiesFromExperienceResponse = {}  # type: ignore[typeddict-item]
    if "FailedEntityList" in data:
        import capo_kendra.types.failed_entity_list

        out["failed_entity_list"] = (
            capo_kendra.types.failed_entity_list.deserialize_aws_json_1_1(
                data["FailedEntityList"]
            )
        )
    return out
