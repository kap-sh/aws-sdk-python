"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListAppliedSchemaArnsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arns
    import aws_sdk_clouddirectory.types.next_token


class ListAppliedSchemaArnsResponse(TypedDict):
    schema_arns: NotRequired["aws_sdk_clouddirectory.types.arns.Arns"]
    """<p>The ARNs of schemas that are applied to the directory.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppliedSchemaArnsResponse) -> dict:
    out: dict = {}
    if "schema_arns" in value:
        import aws_sdk_clouddirectory.types.arns

        out["SchemaArns"] = aws_sdk_clouddirectory.types.arns.serialize_json(
            value["schema_arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppliedSchemaArnsResponse:
    out: ListAppliedSchemaArnsResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArns" in data:
        import aws_sdk_clouddirectory.types.arns

        out["schema_arns"] = aws_sdk_clouddirectory.types.arns.deserialize_json(
            data["SchemaArns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
