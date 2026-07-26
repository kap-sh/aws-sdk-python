"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2CustomHttpHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsWafv2CustomHttpHeader(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the custom header. </p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The value of the custom header. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2CustomHttpHeader) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsWafv2CustomHttpHeader:
    out: AwsWafv2CustomHttpHeader = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
