"""Generated from Smithy shape ``com.amazonaws.glue#BackfillError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.backfill_error_code
    import aws_sdk_glue.types.backfill_errored_partitions_list


class BackfillError(TypedDict):
    code: NotRequired["aws_sdk_glue.types.backfill_error_code.BackfillErrorCode"]
    """<p>The error code for an error that occurred when registering partition indexes for an existing table.</p>"""
    partitions: NotRequired[
        "aws_sdk_glue.types.backfill_errored_partitions_list.BackfillErroredPartitionsList"
    ]
    """<p>A list of a limited number of partitions in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillError) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_glue.types.backfill_error_code

        out["Code"] = aws_sdk_glue.types.backfill_error_code.serialize_aws_json_1_1(
            value["code"]
        )
    if "partitions" in value:
        import aws_sdk_glue.types.backfill_errored_partitions_list

        out["Partitions"] = (
            aws_sdk_glue.types.backfill_errored_partitions_list.serialize_aws_json_1_1(
                value["partitions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BackfillError:
    out: BackfillError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_glue.types.backfill_error_code

        out["code"] = aws_sdk_glue.types.backfill_error_code.deserialize_aws_json_1_1(
            data["Code"]
        )
    if "Partitions" in data:
        import aws_sdk_glue.types.backfill_errored_partitions_list

        out["partitions"] = (
            aws_sdk_glue.types.backfill_errored_partitions_list.deserialize_aws_json_1_1(
                data["Partitions"]
            )
        )
    return out
