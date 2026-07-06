"""Generated from Smithy shape ``com.amazonaws.schemas#DescribeCodeBindingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__timestamp_iso8601
    import aws_sdk_schemas.types.code_generation_status


class DescribeCodeBindingResponse(TypedDict, closed=True):
    creation_date: NotRequired[
        "aws_sdk_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time and date that the code binding was created.</p>"""
    last_modified: NotRequired[
        "aws_sdk_schemas.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time that code bindings were modified.</p>"""
    schema_version: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The version number of the schema.</p>"""
    status: NotRequired[
        "aws_sdk_schemas.types.code_generation_status.CodeGenerationStatus"
    ]
    """<p>The current status of code binding generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCodeBindingResponse) -> dict:
    out: dict = {}
    if "creation_date" in value:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["CreationDate"] = aws_sdk_schemas.types.__timestamp_iso8601.serialize_json(
            value["creation_date"]
        )
    if "last_modified" in value:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["LastModified"] = aws_sdk_schemas.types.__timestamp_iso8601.serialize_json(
            value["last_modified"]
        )
    if "schema_version" in value:
        out["SchemaVersion"] = value["schema_version"]
    if "status" in value:
        import aws_sdk_schemas.types.code_generation_status

        out["Status"] = aws_sdk_schemas.types.code_generation_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCodeBindingResponse:
    out: DescribeCodeBindingResponse = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["creation_date"] = (
            aws_sdk_schemas.types.__timestamp_iso8601.deserialize_json(
                data["CreationDate"]
            )
        )
    if "LastModified" in data:
        import aws_sdk_schemas.types.__timestamp_iso8601

        out["last_modified"] = (
            aws_sdk_schemas.types.__timestamp_iso8601.deserialize_json(
                data["LastModified"]
            )
        )
    if "SchemaVersion" in data:
        out["schema_version"] = data["SchemaVersion"]
    if "Status" in data:
        import aws_sdk_schemas.types.code_generation_status

        out["status"] = aws_sdk_schemas.types.code_generation_status.deserialize_json(
            data["Status"]
        )
    return out
