"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListDevelopmentSchemaArnsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arns
    import capo_clouddirectory.types.next_token


class ListDevelopmentSchemaArnsResponse(TypedDict, closed=True):
    schema_arns: NotRequired["capo_clouddirectory.types.arns.Arns"]
    """<p>The ARNs of retrieved development schemas.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevelopmentSchemaArnsResponse) -> dict:
    out: dict = {}
    if "schema_arns" in value:
        import capo_clouddirectory.types.arns

        out["SchemaArns"] = capo_clouddirectory.types.arns.serialize_json(
            value["schema_arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDevelopmentSchemaArnsResponse:
    out: ListDevelopmentSchemaArnsResponse = {}  # type: ignore[typeddict-item]
    if "SchemaArns" in data:
        import capo_clouddirectory.types.arns

        out["schema_arns"] = capo_clouddirectory.types.arns.deserialize_json(
            data["SchemaArns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
