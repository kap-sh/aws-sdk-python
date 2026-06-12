"""Generated from Smithy shape ``com.amazonaws.schemas#DescribeDiscovererResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__boolean
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.discoverer_state
    import aws_sdk_schemas.types.tags


class DescribeDiscovererResponse(TypedDict):
    description: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The description of the discoverer.</p>"""
    discoverer_arn: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ARN of the discoverer.</p>"""
    discoverer_id: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ID of the discoverer.</p>"""
    source_arn: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ARN of the event bus.</p>"""
    state: NotRequired["aws_sdk_schemas.types.discoverer_state.DiscovererState"]
    """<p>The state of the discoverer.</p>"""
    cross_account: NotRequired["aws_sdk_schemas.types.__boolean.__boolean"]
    """<p>The Status if the discoverer will discover schemas from events sent from another account.</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    """<p>Tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDiscovererResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "discoverer_arn" in value:
        out["DiscovererArn"] = value["discoverer_arn"]
    if "discoverer_id" in value:
        out["DiscovererId"] = value["discoverer_id"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "state" in value:
        import aws_sdk_schemas.types.discoverer_state

        out["State"] = aws_sdk_schemas.types.discoverer_state.serialize_json(
            value["state"]
        )
    if "cross_account" in value:
        out["CrossAccount"] = value["cross_account"]
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeDiscovererResponse:
    out: DescribeDiscovererResponse = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DiscovererArn" in data:
        out["discoverer_arn"] = data["DiscovererArn"]
    if "DiscovererId" in data:
        out["discoverer_id"] = data["DiscovererId"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "State" in data:
        import aws_sdk_schemas.types.discoverer_state

        out["state"] = aws_sdk_schemas.types.discoverer_state.deserialize_json(
            data["State"]
        )
    if "CrossAccount" in data:
        out["cross_account"] = data["CrossAccount"]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    return out
