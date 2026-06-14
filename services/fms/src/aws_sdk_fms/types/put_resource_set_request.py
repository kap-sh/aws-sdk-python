"""Generated from Smithy shape ``com.amazonaws.fms#PutResourceSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_set
    import aws_sdk_fms.types.tag_list


class PutResourceSetRequest(TypedDict):
    resource_set: "aws_sdk_fms.types.resource_set.ResourceSet"
    """<p>Details about the resource set to be created or updated.></p>"""
    tag_list: NotRequired["aws_sdk_fms.types.tag_list.TagList"]
    r"""<p>Retrieves the tags associated with the specified resource set. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to \"customer\" and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourceSetRequest) -> dict:
    out: dict = {}
    import aws_sdk_fms.types.resource_set

    out["ResourceSet"] = aws_sdk_fms.types.resource_set.serialize_aws_json_1_1(
        value["resource_set"]
    )
    if "tag_list" in value:
        import aws_sdk_fms.types.tag_list

        out["TagList"] = aws_sdk_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourceSetRequest:
    out: PutResourceSetRequest = {}  # type: ignore[typeddict-item]
    if "ResourceSet" in data:
        import aws_sdk_fms.types.resource_set

        out["resource_set"] = aws_sdk_fms.types.resource_set.deserialize_aws_json_1_1(
            data["ResourceSet"]
        )
    else:
        raise DeserializationError("PutResourceSetRequest.resource_set required")
    if "TagList" in data:
        import aws_sdk_fms.types.tag_list

        out["tag_list"] = aws_sdk_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
