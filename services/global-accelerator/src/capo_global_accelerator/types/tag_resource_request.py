"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.resource_arn
    import capo_global_accelerator.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_global_accelerator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Global Accelerator resource to add tags to. An ARN uniquely identifies a resource.</p>"""
    tags: "capo_global_accelerator.types.tags.Tags"
    """<p>The tags to add to a resource. A tag consists of a key and a value that you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_global_accelerator.types.tags

    out["Tags"] = capo_global_accelerator.types.tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_global_accelerator.types.tags

        out["tags"] = capo_global_accelerator.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
