"""Generated from Smithy shape ``com.amazonaws.sqs#BatchResultErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.batch_result_error_entry

BatchResultErrorEntryList: TypeAlias = list[
    "capo_sqs.types.batch_result_error_entry.BatchResultErrorEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchResultErrorEntryList) -> list:
    import capo_sqs.types.batch_result_error_entry

    out: list = []
    for item in value:
        out.append(capo_sqs.types.batch_result_error_entry.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BatchResultErrorEntryList:
    import capo_sqs.types.batch_result_error_entry

    out: BatchResultErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sqs.types.batch_result_error_entry.deserialize_aws_json_1_0(item)
        )
    return out
