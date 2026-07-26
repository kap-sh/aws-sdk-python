"""Generated from Smithy shape ``com.amazonaws.securityhub#Indicator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class Indicator(TypedDict, closed=True):
    key: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the indicator that’s present in the attack sequence finding. </p>"""
    values: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>Values associated with each indicator key. For example, if the indicator key is <code>SUSPICIOUS_NETWORK</code>, then the value will be the name of the network. If the indicator key is <code>ATTACK_TACTIC</code>, then the value will be one of the MITRE tactics.</p>"""
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The title describing the indicator. </p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of indicator. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Indicator) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Values"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["values"]
        )
    if "title" in value:
        out["Title"] = value["title"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Indicator:
    out: Indicator = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import capo_securityhub.types.non_empty_string_list

        out["values"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Values"]
        )
    if "Title" in data:
        out["title"] = data["Title"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
