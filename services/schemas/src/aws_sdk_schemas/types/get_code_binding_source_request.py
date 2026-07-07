"""Generated from Smithy shape ``com.amazonaws.schemas#GetCodeBindingSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class GetCodeBindingSourceRequest(TypedDict, closed=True):
    language: "aws_sdk_schemas.types.__string.__string"
    """<p>The language of the code binding.</p>"""
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    schema_version: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>Specifying this limits the results to only this schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeBindingSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeBindingSourceRequest:
    out: GetCodeBindingSourceRequest = {}  # type: ignore[typeddict-item]
    return out
