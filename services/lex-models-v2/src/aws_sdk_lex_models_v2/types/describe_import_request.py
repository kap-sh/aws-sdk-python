"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeImportRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DescribeImportRequest(TypedDict):
    import_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the import to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeImportRequest:
    out: DescribeImportRequest = {}  # type: ignore[typeddict-item]
    return out
