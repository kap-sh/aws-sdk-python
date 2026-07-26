"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateFeedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_arn
    import capo_elementalinference.types.feed_association
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.feed_status
    import capo_elementalinference.types.get_output_list
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.string_list
    import capo_elementalinference.types.tag_map


class CreateFeedResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.feed_arn.FeedArn"
    """<p>A unique ARN that Elemental Inference assigns to the feed.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name that you specified in the request.</p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>A unique ID that Elemental Inference assigns to the feed.</p>"""
    data_endpoints: "capo_elementalinference.types.string_list.StringList"
    """<p>An array of endpoints for the feed. Typically, there is only one endpoint. The feed receives source media at this endpoint (when the calling application calls PutMedia) and returns the resulting metadata to this endpoint (when the calling application calls GetMetadata). </p>"""
    outputs: "capo_elementalinference.types.get_output_list.GetOutputList"
    """<p>Repeats the outputs that you specified in the request.</p>"""
    status: "capo_elementalinference.types.feed_status.FeedStatus"
    """<p>The current status of the feed. After creation of the feed has succeeded, the status will be AVAILABLE. </p>"""
    association: NotRequired[
        "capo_elementalinference.types.feed_association.FeedAssociation"
    ]
    """<p>The association for this feed. When you create the feed, this property is empty. You must associate a resource with the feed using AssociateFeed or UpdateFeed. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>Any tags that you included when you created the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFeedResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    import capo_elementalinference.types.string_list

    out["dataEndpoints"] = capo_elementalinference.types.string_list.serialize_json(
        value["data_endpoints"]
    )
    import capo_elementalinference.types.get_output_list

    out["outputs"] = capo_elementalinference.types.get_output_list.serialize_json(
        value["outputs"]
    )
    import capo_elementalinference.types.feed_status

    out["status"] = capo_elementalinference.types.feed_status.serialize_json(
        value["status"]
    )
    if "association" in value:
        import capo_elementalinference.types.feed_association

        out["association"] = (
            capo_elementalinference.types.feed_association.serialize_json(
                value["association"]
            )
        )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFeedResponse:
    out: CreateFeedResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateFeedResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFeedResponse.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateFeedResponse.id required")
    if "dataEndpoints" in data:
        import capo_elementalinference.types.string_list

        out["data_endpoints"] = (
            capo_elementalinference.types.string_list.deserialize_json(
                data["dataEndpoints"]
            )
        )
    else:
        raise DeserializationError("CreateFeedResponse.data_endpoints required")
    if "outputs" in data:
        import capo_elementalinference.types.get_output_list

        out["outputs"] = capo_elementalinference.types.get_output_list.deserialize_json(
            data["outputs"]
        )
    else:
        raise DeserializationError("CreateFeedResponse.outputs required")
    if "status" in data:
        import capo_elementalinference.types.feed_status

        out["status"] = capo_elementalinference.types.feed_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateFeedResponse.status required")
    if "association" in data:
        import capo_elementalinference.types.feed_association

        out["association"] = (
            capo_elementalinference.types.feed_association.deserialize_json(
                data["association"]
            )
        )
    if "tags" in data:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
