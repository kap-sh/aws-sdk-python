"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.amazon_resource_name


class DescribeResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeResourcePolicyRequest:
    out: DescribeResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
