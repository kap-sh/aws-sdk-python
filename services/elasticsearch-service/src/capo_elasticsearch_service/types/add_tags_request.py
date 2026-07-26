"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AddTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.arn
    import capo_elasticsearch_service.types.tag_list


class AddTagsRequest(TypedDict, closed=True):
    arn: "capo_elasticsearch_service.types.arn.ARN"
    """<p> Specify the <code>ARN</code> for which you want to add the tags.</p>"""
    tag_list: "capo_elasticsearch_service.types.tag_list.TagList"
    """<p> List of <code>Tag</code> that need to be added for the Elasticsearch domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddTagsRequest) -> dict:
    out: dict = {}
    out["ARN"] = value["arn"]
    import capo_elasticsearch_service.types.tag_list

    out["TagList"] = capo_elasticsearch_service.types.tag_list.serialize_json(
        value["tag_list"]
    )
    return out


def deserialize_json(data: dict) -> AddTagsRequest:
    out: AddTagsRequest = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("AddTagsRequest.arn required")
    if "TagList" in data:
        import capo_elasticsearch_service.types.tag_list

        out["tag_list"] = capo_elasticsearch_service.types.tag_list.deserialize_json(
            data["TagList"]
        )
    else:
        raise DeserializationError("AddTagsRequest.tag_list required")
    return out
