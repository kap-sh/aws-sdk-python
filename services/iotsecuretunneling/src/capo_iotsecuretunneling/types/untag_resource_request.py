"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsecuretunneling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.amazon_resource_name
    import capo_iotsecuretunneling.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The resource ARN.</p>"""
    tag_keys: "capo_iotsecuretunneling.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_iotsecuretunneling.types.tag_key_list

    out["tagKeys"] = capo_iotsecuretunneling.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import capo_iotsecuretunneling.types.tag_key_list

        out["tag_keys"] = (
            capo_iotsecuretunneling.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
