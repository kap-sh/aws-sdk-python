"""Generated from Smithy shape ``com.amazonaws.ecs#ListAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes
    import aws_sdk_ecs.types.string


class ListAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>A list of attribute objects that meet the criteria of the request.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListAttributes</code> request. When the results of a <code>ListAttributes</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAttributesResponse:
    out: ListAttributesResponse = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
