"""Generated from Smithy shape ``com.amazonaws.securityhub#DeleteAutomationRuleV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DeleteAutomationRuleV2Request(TypedDict, closed=True):
    identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the V2 automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAutomationRuleV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAutomationRuleV2Request:
    out: DeleteAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
    return out
