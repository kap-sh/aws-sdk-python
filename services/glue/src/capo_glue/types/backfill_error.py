"""Generated from Smithy shape ``com.amazonaws.glue#BackfillError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.backfill_error_code
    import capo_glue.types.backfill_errored_partitions_list


class BackfillError(TypedDict, closed=True):
    code: NotRequired["capo_glue.types.backfill_error_code.BackfillErrorCode"]
    """<p>The error code for an error that occurred when registering partition indexes for an existing table.</p>"""
    partitions: NotRequired[
        "capo_glue.types.backfill_errored_partitions_list.BackfillErroredPartitionsList"
    ]
    """<p>A list of a limited number of partitions in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillError) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_glue.types.backfill_error_code

        out["Code"] = capo_glue.types.backfill_error_code.serialize_aws_json_1_1(
            value["code"]
        )
    if "partitions" in value:
        import capo_glue.types.backfill_errored_partitions_list

        out["Partitions"] = (
            capo_glue.types.backfill_errored_partitions_list.serialize_aws_json_1_1(
                value["partitions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BackfillError:
    out: BackfillError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_glue.types.backfill_error_code

        out["code"] = capo_glue.types.backfill_error_code.deserialize_aws_json_1_1(
            data["Code"]
        )
    if "Partitions" in data:
        import capo_glue.types.backfill_errored_partitions_list

        out["partitions"] = (
            capo_glue.types.backfill_errored_partitions_list.deserialize_aws_json_1_1(
                data["Partitions"]
            )
        )
    return out
