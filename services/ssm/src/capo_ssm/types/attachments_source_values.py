"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentsSourceValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.attachments_source_value

AttachmentsSourceValues: TypeAlias = list[
    "capo_ssm.types.attachments_source_value.AttachmentsSourceValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentsSourceValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AttachmentsSourceValues:
    return [item for item in data if item is not None]
