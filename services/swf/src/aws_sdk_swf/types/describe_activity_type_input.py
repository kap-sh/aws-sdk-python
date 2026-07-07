"""Generated from Smithy shape ``com.amazonaws.swf#DescribeActivityTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.activity_type
    import aws_sdk_swf.types.domain_name


class DescribeActivityTypeInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which the activity type is registered.</p>"""
    activity_type: "aws_sdk_swf.types.activity_type.ActivityType"
    """<p>The activity type to get information about. Activity types are identified by the <code>name</code> and <code>version</code> that were supplied when the activity was registered.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeActivityTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.activity_type

    out["activityType"] = aws_sdk_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeActivityTypeInput:
    out: DescribeActivityTypeInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("DescribeActivityTypeInput.domain required")
    if "activityType" in data:
        import aws_sdk_swf.types.activity_type

        out["activity_type"] = aws_sdk_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError("DescribeActivityTypeInput.activity_type required")
    return out
