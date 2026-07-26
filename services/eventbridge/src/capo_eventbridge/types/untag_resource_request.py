"""Generated from Smithy shape ``com.amazonaws.eventbridge#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.arn
    import capo_eventbridge.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_eventbridge.types.arn.Arn"
    """<p>The ARN of the EventBridge resource from which you are removing tags.</p>"""
    tag_keys: "capo_eventbridge.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_eventbridge.types.tag_key_list

    out["TagKeys"] = capo_eventbridge.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import capo_eventbridge.types.tag_key_list

        out["tag_keys"] = capo_eventbridge.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
