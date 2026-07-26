"""Generated from Smithy shape ``com.amazonaws.personalize#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_personalize.types.arn.Arn"
    """<p>The resource's Amazon Resource Name (ARN).</p>"""
    tag_keys: "capo_personalize.types.tag_keys.TagKeys"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_personalize.types.tag_keys

    out["tagKeys"] = capo_personalize.types.tag_keys.serialize_aws_json_1_1(
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
        import capo_personalize.types.tag_keys

        out["tag_keys"] = capo_personalize.types.tag_keys.deserialize_aws_json_1_1(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
