"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListManagedSchemaArnsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arns
    import aws_sdk_clouddirectory.types.next_token


class ListManagedSchemaArnsResponse(TypedDict, closed=True):
    schema_arns: NotRequired["aws_sdk_clouddirectory.types.arns.Arns"]
    """<p>The ARNs for all AWS managed schemas.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedSchemaArnsResponse) -> dict:
    out: dict = {}
    if "schema_arns" in value:
        import aws_sdk_clouddirectory.types.arns

        out["SchemaArns"] = aws_sdk_clouddirectory.types.arns.serialize_json(
            value["schema_arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedSchemaArnsResponse:
    out: ListManagedSchemaArnsResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArns" in data:
        import aws_sdk_clouddirectory.types.arns

        out["schema_arns"] = aws_sdk_clouddirectory.types.arns.deserialize_json(
            data["SchemaArns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
