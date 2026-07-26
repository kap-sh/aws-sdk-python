"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FoundByKeyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.request_value_list


class FoundByKeyValue(TypedDict, closed=True):
    key_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>A searchable identifier of a customer profile.</p>"""
    values: NotRequired[
        "capo_customer_profiles.types.request_value_list.requestValueList"
    ]
    """<p>A list of key values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoundByKeyValue) -> dict:
    out: dict = {}
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "values" in value:
        import capo_customer_profiles.types.request_value_list

        out["Values"] = capo_customer_profiles.types.request_value_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> FoundByKeyValue:
    out: FoundByKeyValue = {}  # type: ignore[typeddict-item]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "Values" in data:
        import capo_customer_profiles.types.request_value_list

        out["values"] = (
            capo_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    return out
