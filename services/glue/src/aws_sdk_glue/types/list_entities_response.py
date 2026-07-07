"""Generated from Smithy shape ``com.amazonaws.glue#ListEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.entity_list
    import aws_sdk_glue.types.next_token


class ListEntitiesResponse(TypedDict, closed=True):
    entities: NotRequired["aws_sdk_glue.types.entity_list.EntityList"]
    """<p>A list of <code>Entity</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.next_token.NextToken"]
    """<p>A continuation token, present if the current segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_glue.types.entity_list

        out["Entities"] = aws_sdk_glue.types.entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitiesResponse:
    out: ListEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_glue.types.entity_list

        out["entities"] = aws_sdk_glue.types.entity_list.deserialize_aws_json_1_1(
            data["Entities"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
