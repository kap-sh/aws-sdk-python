"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuthorizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_name


class DescribeAuthorizerRequest(TypedDict):
    authorizer_name: "aws_sdk_iot.types.authorizer_name.AuthorizerName"
    """<p>The name of the authorizer to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAuthorizerRequest:
    out: DescribeAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
