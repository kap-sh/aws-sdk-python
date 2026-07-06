"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_errors


class BatchDeleteTableResponse(TypedDict, closed=True):
    errors: NotRequired["aws_sdk_glue.types.table_errors.TableErrors"]
    """<p>A list of errors encountered in attempting to delete the specified tables.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteTableResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_glue.types.table_errors

        out["Errors"] = aws_sdk_glue.types.table_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteTableResponse:
    out: BatchDeleteTableResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_glue.types.table_errors

        out["errors"] = aws_sdk_glue.types.table_errors.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
