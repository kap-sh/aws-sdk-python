"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class DescribeAppInstanceUserRequest(TypedDict):
    app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceUserRequest:
    out: DescribeAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    return out
