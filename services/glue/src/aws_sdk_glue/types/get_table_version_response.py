"""Generated from Smithy shape ``com.amazonaws.glue#GetTableVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_version


class GetTableVersionResponse(TypedDict):
    table_version: NotRequired["aws_sdk_glue.types.table_version.TableVersion"]
    """<p>The requested table version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableVersionResponse) -> dict:
    out: dict = {}
    if "table_version" in value:
        import aws_sdk_glue.types.table_version

        out["TableVersion"] = aws_sdk_glue.types.table_version.serialize_aws_json_1_1(
            value["table_version"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableVersionResponse:
    out: GetTableVersionResponse = {}  # type: ignore[typeddict-item]
    if "TableVersion" in data:
        import aws_sdk_glue.types.table_version

        out["table_version"] = (
            aws_sdk_glue.types.table_version.deserialize_aws_json_1_1(
                data["TableVersion"]
            )
        )
    return out
