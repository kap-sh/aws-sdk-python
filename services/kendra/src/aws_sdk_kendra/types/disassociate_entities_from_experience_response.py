"""Generated from Smithy shape ``com.amazonaws.kendra#DisassociateEntitiesFromExperienceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.failed_entity_list


class DisassociateEntitiesFromExperienceResponse(TypedDict):
    failed_entity_list: NotRequired[
        "aws_sdk_kendra.types.failed_entity_list.FailedEntityList"
    ]
    """<p>Lists the users or groups in your IAM Identity Center identity source that failed to properly remove access to your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateEntitiesFromExperienceResponse) -> dict:
    out: dict = {}
    if "failed_entity_list" in value:
        import aws_sdk_kendra.types.failed_entity_list

        out["FailedEntityList"] = (
            aws_sdk_kendra.types.failed_entity_list.serialize_aws_json_1_1(
                value["failed_entity_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateEntitiesFromExperienceResponse:
    out: DisassociateEntitiesFromExperienceResponse = {}  # type: ignore[typeddict-item]
    if "FailedEntityList" in data:
        import aws_sdk_kendra.types.failed_entity_list

        out["failed_entity_list"] = (
            aws_sdk_kendra.types.failed_entity_list.deserialize_aws_json_1_1(
                data["FailedEntityList"]
            )
        )
    return out
