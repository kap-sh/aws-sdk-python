"""Generated from Smithy shape ``com.amazonaws.glue#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.policy_json_string
    import aws_sdk_glue.types.timestamp


class GetResourcePolicyResponse(TypedDict, closed=True):
    policy_in_json: NotRequired[
        "aws_sdk_glue.types.policy_json_string.PolicyJsonString"
    ]
    """<p>Contains the requested policy document, in JSON format.</p>"""
    policy_hash: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>Contains the hash value associated with this policy.</p>"""
    create_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time at which the policy was created.</p>"""
    update_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time at which the policy was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_in_json" in value:
        out["PolicyInJson"] = value["policy_in_json"]
    if "policy_hash" in value:
        out["PolicyHash"] = value["policy_hash"]
    if "create_time" in value:
        import aws_sdk_glue.types.timestamp

        out["CreateTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "update_time" in value:
        import aws_sdk_glue.types.timestamp

        out["UpdateTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["update_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyInJson" in data:
        out["policy_in_json"] = data["PolicyInJson"]
    if "PolicyHash" in data:
        out["policy_hash"] = data["PolicyHash"]
    if "CreateTime" in data:
        import aws_sdk_glue.types.timestamp

        out["create_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "UpdateTime" in data:
        import aws_sdk_glue.types.timestamp

        out["update_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["UpdateTime"]
        )
    return out
