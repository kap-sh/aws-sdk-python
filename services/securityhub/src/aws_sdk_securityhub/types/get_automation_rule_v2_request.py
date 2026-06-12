"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAutomationRuleV2Request``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class GetAutomationRuleV2Request(TypedDict):
    identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the V2 automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomationRuleV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomationRuleV2Request:
    out: GetAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
    return out
