"""Generated from Smithy shape ``com.amazonaws.ssm#CreateAssociationBatchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_description_list
    import aws_sdk_ssm.types.failed_create_association_list


class CreateAssociationBatchResult(TypedDict, closed=True):
    successful: NotRequired[
        "aws_sdk_ssm.types.association_description_list.AssociationDescriptionList"
    ]
    """<p>Information about the associations that succeeded.</p>"""
    failed: NotRequired[
        "aws_sdk_ssm.types.failed_create_association_list.FailedCreateAssociationList"
    ]
    """<p>Information about the associations that failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssociationBatchResult) -> dict:
    out: dict = {}
    if "successful" in value:
        import aws_sdk_ssm.types.association_description_list

        out["Successful"] = (
            aws_sdk_ssm.types.association_description_list.serialize_aws_json_1_1(
                value["successful"]
            )
        )
    if "failed" in value:
        import aws_sdk_ssm.types.failed_create_association_list

        out["Failed"] = (
            aws_sdk_ssm.types.failed_create_association_list.serialize_aws_json_1_1(
                value["failed"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAssociationBatchResult:
    out: CreateAssociationBatchResult = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_ssm.types.association_description_list

        out["successful"] = (
            aws_sdk_ssm.types.association_description_list.deserialize_aws_json_1_1(
                data["Successful"]
            )
        )
    if "Failed" in data:
        import aws_sdk_ssm.types.failed_create_association_list

        out["failed"] = (
            aws_sdk_ssm.types.failed_create_association_list.deserialize_aws_json_1_1(
                data["Failed"]
            )
        )
    return out
