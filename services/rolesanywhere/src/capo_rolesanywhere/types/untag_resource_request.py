"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.amazon_resource_name
    import capo_rolesanywhere.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rolesanywhere.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "capo_rolesanywhere.types.tag_key_list.TagKeyList"
    """<p>A list of keys. Tag keys are the unique identifiers of tags. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_rolesanywhere.types.tag_key_list

    out["tagKeys"] = capo_rolesanywhere.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import capo_rolesanywhere.types.tag_key_list

        out["tag_keys"] = capo_rolesanywhere.types.tag_key_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
