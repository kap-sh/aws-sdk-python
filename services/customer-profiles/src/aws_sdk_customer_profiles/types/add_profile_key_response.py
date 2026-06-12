"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AddProfileKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.request_value_list


class AddProfileKeyResponse(TypedDict):
    key_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>A searchable identifier of a customer profile.</p>"""
    values: NotRequired[
        "aws_sdk_customer_profiles.types.request_value_list.requestValueList"
    ]
    """<p>A list of key values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddProfileKeyResponse) -> dict:
    out: dict = {}
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "values" in value:
        import aws_sdk_customer_profiles.types.request_value_list

        out["Values"] = (
            aws_sdk_customer_profiles.types.request_value_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddProfileKeyResponse:
    out: AddProfileKeyResponse = {}  # type: ignore[typeddict-item]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "Values" in data:
        import aws_sdk_customer_profiles.types.request_value_list

        out["values"] = (
            aws_sdk_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    return out
