"""Generated from Smithy shape ``com.amazonaws.ssm#StartAccessRequestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string1to256
    import aws_sdk_ssm.types.tag_list
    import aws_sdk_ssm.types.targets


class StartAccessRequestRequest(TypedDict):
    reason: "aws_sdk_ssm.types.string1to256.String1to256"
    """<p>A brief description explaining why you are requesting access to the node.</p>"""
    targets: "aws_sdk_ssm.types.targets.Targets"
    """<p>The node you are requesting access to.</p>"""
    tags: NotRequired["aws_sdk_ssm.types.tag_list.TagList"]
    """<p>Key-value pairs of metadata you want to assign to the access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAccessRequestRequest) -> dict:
    out: dict = {}
    out["Reason"] = value["reason"]
    import aws_sdk_ssm.types.targets

    out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "tags" in value:
        import aws_sdk_ssm.types.tag_list

        out["Tags"] = aws_sdk_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAccessRequestRequest:
    out: StartAccessRequestRequest = {}  # type: ignore[typeddict-item]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("StartAccessRequestRequest.reason required")
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        raise DeserializationError("StartAccessRequestRequest.targets required")
    if "Tags" in data:
        import aws_sdk_ssm.types.tag_list

        out["tags"] = aws_sdk_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
