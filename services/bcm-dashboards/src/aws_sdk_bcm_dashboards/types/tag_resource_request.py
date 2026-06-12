"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.resource_arn
    import aws_sdk_bcm_dashboards.types.resource_tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bcm_dashboards.types.resource_arn.ResourceArn"
    """<p>The unique identifier for the resource.</p>"""
    resource_tags: "aws_sdk_bcm_dashboards.types.resource_tag_list.ResourceTagList"
    """<p>The tags to add to the dashboard resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_bcm_dashboards.types.resource_tag_list

    out["resourceTags"] = (
        aws_sdk_bcm_dashboards.types.resource_tag_list.serialize_aws_json_1_0(
            value["resource_tags"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "resourceTags" in data:
        import aws_sdk_bcm_dashboards.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_bcm_dashboards.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.resource_tags required")
    return out
