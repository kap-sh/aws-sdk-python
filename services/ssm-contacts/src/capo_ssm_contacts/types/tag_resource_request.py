"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.amazon_resource_name
    import capo_ssm_contacts.types.tags_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ssm_contacts.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""
    tags: "capo_ssm_contacts.types.tags_list.TagsList"
    """<p>A list of tags that you are adding to the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_ssm_contacts.types.tags_list

    out["Tags"] = capo_ssm_contacts.types.tags_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_ssm_contacts.types.tags_list

        out["tags"] = capo_ssm_contacts.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
