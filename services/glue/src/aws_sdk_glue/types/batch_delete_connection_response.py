"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeleteConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_by_name
    import aws_sdk_glue.types.name_string_list


class BatchDeleteConnectionResponse(TypedDict, closed=True):
    succeeded: NotRequired["aws_sdk_glue.types.name_string_list.NameStringList"]
    """<p>A list of names of the connection definitions that were successfully deleted.</p>"""
    errors: NotRequired["aws_sdk_glue.types.error_by_name.ErrorByName"]
    """<p>A map of the names of connections that were not successfully deleted to error details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteConnectionResponse) -> dict:
    out: dict = {}
    if "succeeded" in value:
        import aws_sdk_glue.types.name_string_list

        out["Succeeded"] = aws_sdk_glue.types.name_string_list.serialize_aws_json_1_1(
            value["succeeded"]
        )
    if "errors" in value:
        import aws_sdk_glue.types.error_by_name

        out["Errors"] = aws_sdk_glue.types.error_by_name.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteConnectionResponse:
    out: BatchDeleteConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Succeeded" in data:
        import aws_sdk_glue.types.name_string_list

        out["succeeded"] = aws_sdk_glue.types.name_string_list.deserialize_aws_json_1_1(
            data["Succeeded"]
        )
    if "Errors" in data:
        import aws_sdk_glue.types.error_by_name

        out["errors"] = aws_sdk_glue.types.error_by_name.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
