"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.long
    import aws_sdk_config_service.types.resource_type


class ResourceCount(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.resource_type.ResourceType"
    ]
    r"""<p>The resource type (for example, <code>\"AWS::EC2::Instance\"</code>).</p>"""
    count: "aws_sdk_config_service.types.long.Long"
    """<p>The number of resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCount) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_config_service.types.resource_type

        out["resourceType"] = (
            aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    out["count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceCount:
    out: ResourceCount = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_config_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
