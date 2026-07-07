"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateFeedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.feed_arn
    import aws_sdk_elementalinference.types.feed_association
    import aws_sdk_elementalinference.types.feed_id
    import aws_sdk_elementalinference.types.feed_status
    import aws_sdk_elementalinference.types.get_output_list
    import aws_sdk_elementalinference.types.resource_name
    import aws_sdk_elementalinference.types.string_list
    import aws_sdk_elementalinference.types.tag_map


class UpdateFeedResponse(TypedDict, closed=True):
    arn: "aws_sdk_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the feed.</p>"""
    name: "aws_sdk_elementalinference.types.resource_name.ResourceName"
    """<p>The updated or original name of the feed.</p>"""
    id: "aws_sdk_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""
    data_endpoints: "aws_sdk_elementalinference.types.string_list.StringList"
    """<p>The data endpoints of the feed.</p>"""
    outputs: "aws_sdk_elementalinference.types.get_output_list.GetOutputList"
    """<p>The array of outputs in the feed. You might have left this array unchanged, or you might have changed it. </p>"""
    status: "aws_sdk_elementalinference.types.feed_status.FeedStatus"
    """<p>The status of the feed.</p>"""
    association: NotRequired[
        "aws_sdk_elementalinference.types.feed_association.FeedAssociation"
    ]
    """<p>Information about the resource that is associated with the feed, if any.</p>"""
    tags: NotRequired["aws_sdk_elementalinference.types.tag_map.TagMap"]
    """<p>The tags associated with the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFeedResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    import aws_sdk_elementalinference.types.string_list

    out["dataEndpoints"] = aws_sdk_elementalinference.types.string_list.serialize_json(
        value["data_endpoints"]
    )
    import aws_sdk_elementalinference.types.get_output_list

    out["outputs"] = aws_sdk_elementalinference.types.get_output_list.serialize_json(
        value["outputs"]
    )
    import aws_sdk_elementalinference.types.feed_status

    out["status"] = aws_sdk_elementalinference.types.feed_status.serialize_json(
        value["status"]
    )
    if "association" in value:
        import aws_sdk_elementalinference.types.feed_association

        out["association"] = (
            aws_sdk_elementalinference.types.feed_association.serialize_json(
                value["association"]
            )
        )
    if "tags" in value:
        import aws_sdk_elementalinference.types.tag_map

        out["tags"] = aws_sdk_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFeedResponse:
    out: UpdateFeedResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateFeedResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateFeedResponse.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateFeedResponse.id required")
    if "dataEndpoints" in data:
        import aws_sdk_elementalinference.types.string_list

        out["data_endpoints"] = (
            aws_sdk_elementalinference.types.string_list.deserialize_json(
                data["dataEndpoints"]
            )
        )
    else:
        raise DeserializationError("UpdateFeedResponse.data_endpoints required")
    if "outputs" in data:
        import aws_sdk_elementalinference.types.get_output_list

        out["outputs"] = (
            aws_sdk_elementalinference.types.get_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        raise DeserializationError("UpdateFeedResponse.outputs required")
    if "status" in data:
        import aws_sdk_elementalinference.types.feed_status

        out["status"] = aws_sdk_elementalinference.types.feed_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateFeedResponse.status required")
    if "association" in data:
        import aws_sdk_elementalinference.types.feed_association

        out["association"] = (
            aws_sdk_elementalinference.types.feed_association.deserialize_json(
                data["association"]
            )
        )
    if "tags" in data:
        import aws_sdk_elementalinference.types.tag_map

        out["tags"] = aws_sdk_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
