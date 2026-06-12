"""Generated from Smithy shape ``com.amazonaws.ssm#CreateAssociationBatchRequestEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.create_association_batch_request_entry

CreateAssociationBatchRequestEntries: TypeAlias = list[
    "aws_sdk_ssm.types.create_association_batch_request_entry.CreateAssociationBatchRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAssociationBatchRequestEntries) -> list:
    import aws_sdk_ssm.types.create_association_batch_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.create_association_batch_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CreateAssociationBatchRequestEntries:
    import aws_sdk_ssm.types.create_association_batch_request_entry

    out: CreateAssociationBatchRequestEntries = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.create_association_batch_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
