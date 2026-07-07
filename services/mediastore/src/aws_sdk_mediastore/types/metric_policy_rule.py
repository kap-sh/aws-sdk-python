"""Generated from Smithy shape ``com.amazonaws.mediastore#MetricPolicyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.object_group
    import aws_sdk_mediastore.types.object_group_name


class MetricPolicyRule(TypedDict, closed=True):
    object_group: "aws_sdk_mediastore.types.object_group.ObjectGroup"
    """<p>A path or file name that defines which objects to include in the group. Wildcards (*) are acceptable.</p>"""
    object_group_name: "aws_sdk_mediastore.types.object_group_name.ObjectGroupName"
    """<p>A name that allows you to refer to the object group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricPolicyRule) -> dict:
    out: dict = {}
    out["ObjectGroup"] = value["object_group"]
    out["ObjectGroupName"] = value["object_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricPolicyRule:
    out: MetricPolicyRule = {}  # type: ignore[typeddict-item]
    if "ObjectGroup" in data:
        out["object_group"] = data["ObjectGroup"]
    else:
        raise DeserializationError("MetricPolicyRule.object_group required")
    if "ObjectGroupName" in data:
        out["object_group_name"] = data["ObjectGroupName"]
    else:
        raise DeserializationError("MetricPolicyRule.object_group_name required")
    return out
