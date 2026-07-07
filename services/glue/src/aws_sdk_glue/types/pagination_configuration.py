"""Generated from Smithy shape ``com.amazonaws.glue#PaginationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.cursor_configuration
    import aws_sdk_glue.types.offset_configuration


class PaginationConfiguration(TypedDict, closed=True):
    cursor_configuration: NotRequired[
        "aws_sdk_glue.types.cursor_configuration.CursorConfiguration"
    ]
    """<p>Configuration for cursor-based pagination, where the API provides a cursor or token to retrieve the next page of results.</p>"""
    offset_configuration: NotRequired[
        "aws_sdk_glue.types.offset_configuration.OffsetConfiguration"
    ]
    """<p>Configuration for offset-based pagination, where the API uses numeric offsets and limits to control which results are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PaginationConfiguration) -> dict:
    out: dict = {}
    if "cursor_configuration" in value:
        import aws_sdk_glue.types.cursor_configuration

        out["CursorConfiguration"] = (
            aws_sdk_glue.types.cursor_configuration.serialize_aws_json_1_1(
                value["cursor_configuration"]
            )
        )
    if "offset_configuration" in value:
        import aws_sdk_glue.types.offset_configuration

        out["OffsetConfiguration"] = (
            aws_sdk_glue.types.offset_configuration.serialize_aws_json_1_1(
                value["offset_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PaginationConfiguration:
    out: PaginationConfiguration = {}  # type: ignore[typeddict-item]
    if "CursorConfiguration" in data:
        import aws_sdk_glue.types.cursor_configuration

        out["cursor_configuration"] = (
            aws_sdk_glue.types.cursor_configuration.deserialize_aws_json_1_1(
                data["CursorConfiguration"]
            )
        )
    if "OffsetConfiguration" in data:
        import aws_sdk_glue.types.offset_configuration

        out["offset_configuration"] = (
            aws_sdk_glue.types.offset_configuration.deserialize_aws_json_1_1(
                data["OffsetConfiguration"]
            )
        )
    return out
