"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupPrefixListId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2SecurityGroupPrefixListId(TypedDict, closed=True):
    prefix_list_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupPrefixListId) -> dict:
    out: dict = {}
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2SecurityGroupPrefixListId:
    out: AwsEc2SecurityGroupPrefixListId = {}  # type: ignore[typeddict-item]
    if "PrefixListId" in data:
        out["prefix_list_id"] = data["PrefixListId"]
    return out
