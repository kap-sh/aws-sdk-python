"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetActivationJobSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.start_read_set_activation_job_source_item

StartReadSetActivationJobSourceList: TypeAlias = list[
    "aws_sdk_omics.types.start_read_set_activation_job_source_item.StartReadSetActivationJobSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetActivationJobSourceList) -> list:
    import aws_sdk_omics.types.start_read_set_activation_job_source_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.start_read_set_activation_job_source_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartReadSetActivationJobSourceList:
    import aws_sdk_omics.types.start_read_set_activation_job_source_item

    out: StartReadSetActivationJobSourceList = []
    for item in data:
        out.append(
            aws_sdk_omics.types.start_read_set_activation_job_source_item.deserialize_json(
                item
            )
        )
    return out
