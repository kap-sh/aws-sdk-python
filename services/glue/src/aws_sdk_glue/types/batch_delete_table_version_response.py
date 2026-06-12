"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteTableVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_version_errors


class BatchDeleteTableVersionResponse(TypedDict):
    errors: NotRequired["aws_sdk_glue.types.table_version_errors.TableVersionErrors"]
    """<p>A list of errors encountered while trying to delete the specified table versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteTableVersionResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_glue.types.table_version_errors

        out["Errors"] = aws_sdk_glue.types.table_version_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteTableVersionResponse:
    out: BatchDeleteTableVersionResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_glue.types.table_version_errors

        out["errors"] = (
            aws_sdk_glue.types.table_version_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
