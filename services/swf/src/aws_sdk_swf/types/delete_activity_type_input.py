"""Generated from Smithy shape ``com.amazonaws.swf#DeleteActivityTypeInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.activity_type
    import aws_sdk_swf.types.domain_name


class DeleteActivityTypeInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which the activity type is registered.</p>"""
    activity_type: "aws_sdk_swf.types.activity_type.ActivityType"
    """<p>The activity type to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteActivityTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.activity_type

    out["activityType"] = aws_sdk_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteActivityTypeInput:
    out: DeleteActivityTypeInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("DeleteActivityTypeInput.domain required")
    if "activityType" in data:
        import aws_sdk_swf.types.activity_type

        out["activity_type"] = aws_sdk_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError("DeleteActivityTypeInput.activity_type required")
    return out
