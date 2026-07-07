"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTableOptimizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_get_table_optimizer_entries


class BatchGetTableOptimizerRequest(TypedDict, closed=True):
    entries: "aws_sdk_glue.types.batch_get_table_optimizer_entries.BatchGetTableOptimizerEntries"
    """<p>A list of <code>BatchGetTableOptimizerEntry</code> objects specifying the table optimizers to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTableOptimizerRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.batch_get_table_optimizer_entries

    out["Entries"] = (
        aws_sdk_glue.types.batch_get_table_optimizer_entries.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetTableOptimizerRequest:
    out: BatchGetTableOptimizerRequest = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_glue.types.batch_get_table_optimizer_entries

        out["entries"] = (
            aws_sdk_glue.types.batch_get_table_optimizer_entries.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("BatchGetTableOptimizerRequest.entries required")
    return out
