"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.type_list


class SecurityControlParameter(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of a </p>"""
    value: NotRequired["capo_securityhub.types.type_list.TypeList"]
    """<p> The current value of a control parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        import capo_securityhub.types.type_list

        out["Value"] = capo_securityhub.types.type_list.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> SecurityControlParameter:
    out: SecurityControlParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        import capo_securityhub.types.type_list

        out["value"] = capo_securityhub.types.type_list.deserialize_json(data["Value"])
    return out
