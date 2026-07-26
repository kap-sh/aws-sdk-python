"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.taggable_resource_arn
    import capo_partnercentral_benefits.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_benefits.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "capo_partnercentral_benefits.types.tags.Tags"
    """<p>A list of key-value pairs to add as tags to the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_partnercentral_benefits.types.tags

    out["tags"] = capo_partnercentral_benefits.types.tags.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import capo_partnercentral_benefits.types.tags

        out["tags"] = capo_partnercentral_benefits.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
