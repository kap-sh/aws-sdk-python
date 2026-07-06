"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.resource_arn
    import aws_sdk_bcm_dashboards.types.resource_tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_bcm_dashboards.types.resource_arn.ResourceArn"
    """<p>The unique identifier for the resource.</p>"""
    resource_tag_keys: (
        "aws_sdk_bcm_dashboards.types.resource_tag_key_list.ResourceTagKeyList"
    )
    """<p>The keys of the tags to remove from the dashboard resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_bcm_dashboards.types.resource_tag_key_list

    out["resourceTagKeys"] = (
        aws_sdk_bcm_dashboards.types.resource_tag_key_list.serialize_aws_json_1_0(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "resourceTagKeys" in data:
        import aws_sdk_bcm_dashboards.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            aws_sdk_bcm_dashboards.types.resource_tag_key_list.deserialize_aws_json_1_0(
                data["resourceTagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.resource_tag_keys required")
    return out
