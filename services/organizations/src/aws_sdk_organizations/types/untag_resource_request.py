"""Generated from Smithy shape ``com.amazonaws.organizations#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.tag_keys
    import aws_sdk_organizations.types.taggable_resource_id


class UntagResourceRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_organizations.types.taggable_resource_id.TaggableResourceId"
    """<p>The ID of the resource to remove a tag from.</p> <p>You can specify any of the following taggable resources.</p> <ul> <li> <p>Amazon Web Services account – specify the account ID number.</p> </li> <li> <p>Organizational unit – specify the OU ID that begins with <code>ou-</code> and looks similar to: <code>ou-<i>1a2b-34uvwxyz</i> </code> </p> </li> <li> <p>Root – specify the root ID that begins with <code>r-</code> and looks similar to: <code>r-<i>1a2b</i> </code> </p> </li> <li> <p>Policy – specify the policy ID that begins with <code>p-</code> andlooks similar to: <code>p-<i>12abcdefg3</i> </code> </p> </li> </ul>"""
    tag_keys: "aws_sdk_organizations.types.tag_keys.TagKeys"
    """<p>The list of keys for tags to remove from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_organizations.types.tag_keys

    out["TagKeys"] = aws_sdk_organizations.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_id required")
    if "TagKeys" in data:
        import aws_sdk_organizations.types.tag_keys

        out["tag_keys"] = aws_sdk_organizations.types.tag_keys.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
