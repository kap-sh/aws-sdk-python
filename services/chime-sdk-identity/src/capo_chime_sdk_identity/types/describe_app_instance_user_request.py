"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn


class DescribeAppInstanceUserRequest(TypedDict, closed=True):
    app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceUserRequest:
    out: DescribeAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    return out
