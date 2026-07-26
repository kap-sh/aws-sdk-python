"""Generated from Smithy shape ``com.amazonaws.athena#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.amazon_resource_name
    import capo_athena.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>Specifies the ARN of the Athena resource to which tags are to be added.</p>"""
    tags: "capo_athena.types.tag_list.TagList"
    """<p>A collection of one or more tags, separated by commas, to be added to an Athena resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_athena.types.tag_list

    out["Tags"] = capo_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import capo_athena.types.tag_list

        out["tags"] = capo_athena.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
