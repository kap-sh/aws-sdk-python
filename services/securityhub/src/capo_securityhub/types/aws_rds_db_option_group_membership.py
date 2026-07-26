"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbOptionGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsRdsDbOptionGroupMembership(TypedDict, closed=True):
    option_group_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the option group.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the option group membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbOptionGroupMembership) -> dict:
    out: dict = {}
    if "option_group_name" in value:
        out["OptionGroupName"] = value["option_group_name"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbOptionGroupMembership:
    out: AwsRdsDbOptionGroupMembership = {}  # type: ignore[typeddict-item]
    if "OptionGroupName" in data:
        out["option_group_name"] = data["OptionGroupName"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
