"""Generated from Smithy shape ``com.amazonaws.fms#PutPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.policy
    import aws_sdk_fms.types.tag_list


class PutPolicyRequest(TypedDict, closed=True):
    policy: "aws_sdk_fms.types.policy.Policy"
    """<p>The details of the Firewall Manager policy to be created.</p>"""
    tag_list: NotRequired["aws_sdk_fms.types.tag_list.TagList"]
    """<p>The tags to add to the Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPolicyRequest) -> dict:
    out: dict = {}
    import aws_sdk_fms.types.policy

    out["Policy"] = aws_sdk_fms.types.policy.serialize_aws_json_1_1(value["policy"])
    if "tag_list" in value:
        import aws_sdk_fms.types.tag_list

        out["TagList"] = aws_sdk_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPolicyRequest:
    out: PutPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        import aws_sdk_fms.types.policy

        out["policy"] = aws_sdk_fms.types.policy.deserialize_aws_json_1_1(
            data["Policy"]
        )
    else:
        raise DeserializationError("PutPolicyRequest.policy required")
    if "TagList" in data:
        import aws_sdk_fms.types.tag_list

        out["tag_list"] = aws_sdk_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
