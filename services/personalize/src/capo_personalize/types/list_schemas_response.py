"""Generated from Smithy shape ``com.amazonaws.personalize#ListSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.next_token
    import capo_personalize.types.schemas


class ListSchemasResponse(TypedDict, closed=True):
    schemas: NotRequired["capo_personalize.types.schemas.Schemas"]
    """<p>A list of schemas.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token used to get the next set of schemas (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasResponse) -> dict:
    out: dict = {}
    if "schemas" in value:
        import capo_personalize.types.schemas

        out["schemas"] = capo_personalize.types.schemas.serialize_aws_json_1_1(
            value["schemas"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasResponse:
    out: ListSchemasResponse = {}  # type: ignore[typeddict-item]
    if "schemas" in data:
        import capo_personalize.types.schemas

        out["schemas"] = capo_personalize.types.schemas.deserialize_aws_json_1_1(
            data["schemas"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
