"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceAdminRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn


class DescribeAppInstanceAdminRequest(TypedDict):
    app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceAdmin</code>.</p>"""
    app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceAdminRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceAdminRequest:
    out: DescribeAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
    return out
