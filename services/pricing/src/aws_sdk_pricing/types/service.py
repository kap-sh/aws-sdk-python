"""Generated from Smithy shape ``com.amazonaws.pricing#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pricing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pricing.types.attribute_name_list
    import aws_sdk_pricing.types.string


class Service(TypedDict, closed=True):
    service_code: "aws_sdk_pricing.types.string.String"
    """<p>The code for the Amazon Web Services service.</p>"""
    attribute_names: NotRequired[
        "aws_sdk_pricing.types.attribute_name_list.AttributeNameList"
    ]
    """<p>The attributes that are available for this service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Service) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    if "attribute_names" in value:
        import aws_sdk_pricing.types.attribute_name_list

        out["AttributeNames"] = (
            aws_sdk_pricing.types.attribute_name_list.serialize_aws_json_1_1(
                value["attribute_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError("Service.service_code required")
    if "AttributeNames" in data:
        import aws_sdk_pricing.types.attribute_name_list

        out["attribute_names"] = (
            aws_sdk_pricing.types.attribute_name_list.deserialize_aws_json_1_1(
                data["AttributeNames"]
            )
        )
    return out
