"""Generated from Smithy shape ``com.amazonaws.swf#UndeprecateActivityTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.activity_type
    import aws_sdk_swf.types.domain_name


class UndeprecateActivityTypeInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain of the deprecated activity type.</p>"""
    activity_type: "aws_sdk_swf.types.activity_type.ActivityType"
    """<p>The activity type to undeprecate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UndeprecateActivityTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.activity_type

    out["activityType"] = aws_sdk_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UndeprecateActivityTypeInput:
    out: UndeprecateActivityTypeInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("UndeprecateActivityTypeInput.domain required")
    if "activityType" in data:
        import aws_sdk_swf.types.activity_type

        out["activity_type"] = aws_sdk_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError(
            "UndeprecateActivityTypeInput.activity_type required"
        )
    return out
