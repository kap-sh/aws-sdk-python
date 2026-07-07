"""Generated from Smithy shape ``com.amazonaws.securityhub#StatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class StatusReason(TypedDict, closed=True):
    reason_code: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>A code that represents a reason for the control status. For the list of status reason codes and their meanings, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-asff-compliance\">Compliance details for control findings</a> in the <i>Security Hub CSPM User Guide</i>. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The corresponding description for the status reason code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> dict:
    out: dict = {}
    if "reason_code" in value:
        out["ReasonCode"] = value["reason_code"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StatusReason:
    out: StatusReason = {}  # type: ignore[typeddict-item]
    if "ReasonCode" in data:
        out["reason_code"] = data["ReasonCode"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
