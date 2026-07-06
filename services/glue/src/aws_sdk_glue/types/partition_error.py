"""Generated from Smithy shape ``com.amazonaws.glue#PartitionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.value_string_list


class PartitionError(TypedDict, closed=True):
    partition_values: NotRequired[
        "aws_sdk_glue.types.value_string_list.ValueStringList"
    ]
    """<p>The values that define the partition.</p>"""
    error_detail: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>The details about the partition error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionError) -> dict:
    out: dict = {}
    if "partition_values" in value:
        import aws_sdk_glue.types.value_string_list

        out["PartitionValues"] = (
            aws_sdk_glue.types.value_string_list.serialize_aws_json_1_1(
                value["partition_values"]
            )
        )
    if "error_detail" in value:
        import aws_sdk_glue.types.error_detail

        out["ErrorDetail"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionError:
    out: PartitionError = {}  # type: ignore[typeddict-item]
    if "PartitionValues" in data:
        import aws_sdk_glue.types.value_string_list

        out["partition_values"] = (
            aws_sdk_glue.types.value_string_list.deserialize_aws_json_1_1(
                data["PartitionValues"]
            )
        )
    if "ErrorDetail" in data:
        import aws_sdk_glue.types.error_detail

        out["error_detail"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["ErrorDetail"]
        )
    return out
