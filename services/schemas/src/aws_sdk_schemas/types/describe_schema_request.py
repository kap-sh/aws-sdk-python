"""Generated from Smithy shape ``com.amazonaws.schemas#DescribeSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class DescribeSchemaRequest(TypedDict, closed=True):
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only this schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSchemaRequest:
    out: DescribeSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
