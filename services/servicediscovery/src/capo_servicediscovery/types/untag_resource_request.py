"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.amazon_resource_name
    import capo_servicediscovery.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_servicediscovery.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.</p>"""
    tag_keys: "capo_servicediscovery.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_servicediscovery.types.tag_key_list

    out["TagKeys"] = capo_servicediscovery.types.tag_key_list.serialize_aws_json_1_1(
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
        import capo_servicediscovery.types.tag_key_list

        out["tag_keys"] = (
            capo_servicediscovery.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
