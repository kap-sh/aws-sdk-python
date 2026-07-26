"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFeedResponse``."""

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


class GetFeedResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.feed_arn.FeedArn"
    """<p>The ARN of the feed.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the feed.</p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed.</p>"""
    data_endpoints: "capo_elementalinference.types.string_list.StringList"
    """<p>The dataEndpoints of the feed.</p>"""
    outputs: "capo_elementalinference.types.get_output_list.GetOutputList"
    """<p>An array of the outputs in the feed.</p>"""
    status: "capo_elementalinference.types.feed_status.FeedStatus"
    """<p>The status of the feed.</p>"""
    association: NotRequired[
        "capo_elementalinference.types.feed_association.FeedAssociation"
    ]
    """<p>Information about the resource that is associated with the feed. It's possible that there is no associated resource. This is not an error. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>A list of the tags, if any, for the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFeedResponse) -> dict:
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


def deserialize_json(data: dict) -> GetFeedResponse:
    out: GetFeedResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetFeedResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetFeedResponse.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetFeedResponse.id required")
    if "dataEndpoints" in data:
        import capo_elementalinference.types.string_list

        out["data_endpoints"] = (
            capo_elementalinference.types.string_list.deserialize_json(
                data["dataEndpoints"]
            )
        )
    else:
        raise DeserializationError("GetFeedResponse.data_endpoints required")
    if "outputs" in data:
        import capo_elementalinference.types.get_output_list

        out["outputs"] = capo_elementalinference.types.get_output_list.deserialize_json(
            data["outputs"]
        )
    else:
        raise DeserializationError("GetFeedResponse.outputs required")
    if "status" in data:
        import capo_elementalinference.types.feed_status

        out["status"] = capo_elementalinference.types.feed_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetFeedResponse.status required")
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
