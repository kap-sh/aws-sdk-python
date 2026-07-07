"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetBatchImportJobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.batch_import_list
    import aws_sdk_frauddetector.types.string


class GetBatchImportJobsResult(TypedDict, closed=True):
    batch_imports: NotRequired[
        "aws_sdk_frauddetector.types.batch_import_list.BatchImportList"
    ]
    """<p>An array containing the details of each batch import job.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next token for the subsequent resquest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBatchImportJobsResult) -> dict:
    out: dict = {}
    if "batch_imports" in value:
        import aws_sdk_frauddetector.types.batch_import_list

        out["batchImports"] = (
            aws_sdk_frauddetector.types.batch_import_list.serialize_aws_json_1_1(
                value["batch_imports"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBatchImportJobsResult:
    out: GetBatchImportJobsResult = {}  # type: ignore[typeddict-item]
    if "batchImports" in data:
        import aws_sdk_frauddetector.types.batch_import_list

        out["batch_imports"] = (
            aws_sdk_frauddetector.types.batch_import_list.deserialize_aws_json_1_1(
                data["batchImports"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
