"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AdditionalSearchKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.request_value_list


class AdditionalSearchKey(TypedDict, closed=True):
    key_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile.</p>"""
    values: "aws_sdk_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalSearchKey) -> dict:
    out: dict = {}
    out["KeyName"] = value["key_name"]
    import aws_sdk_customer_profiles.types.request_value_list

    out["Values"] = aws_sdk_customer_profiles.types.request_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> AdditionalSearchKey:
    out: AdditionalSearchKey = {}  # type: ignore[typeddict-item]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("AdditionalSearchKey.key_name required")
    if "Values" in data:
        import aws_sdk_customer_profiles.types.request_value_list

        out["values"] = (
            aws_sdk_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("AdditionalSearchKey.values required")
    return out
