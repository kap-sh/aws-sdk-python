"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIsInAddressList``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ingress_address_list_arn_list
    import aws_sdk_mailmanager.types.ingress_address_list_email_attribute


class IngressIsInAddressList(TypedDict):
    attribute: "aws_sdk_mailmanager.types.ingress_address_list_email_attribute.IngressAddressListEmailAttribute"
    """<p>The email attribute that needs to be evaluated against the address list.</p>"""
    address_lists: "aws_sdk_mailmanager.types.ingress_address_list_arn_list.IngressAddressListArnList"
    """<p>The address lists that will be used for evaluation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIsInAddressList) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ingress_address_list_email_attribute

    out["Attribute"] = (
        aws_sdk_mailmanager.types.ingress_address_list_email_attribute.serialize_aws_json_1_0(
            value["attribute"]
        )
    )
    import aws_sdk_mailmanager.types.ingress_address_list_arn_list

    out["AddressLists"] = (
        aws_sdk_mailmanager.types.ingress_address_list_arn_list.serialize_aws_json_1_0(
            value["address_lists"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressIsInAddressList:
    out: IngressIsInAddressList = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.ingress_address_list_email_attribute

        out["attribute"] = (
            aws_sdk_mailmanager.types.ingress_address_list_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        )
    else:
        raise DeserializationError("IngressIsInAddressList.attribute required")
    if "AddressLists" in data:
        import aws_sdk_mailmanager.types.ingress_address_list_arn_list

        out["address_lists"] = (
            aws_sdk_mailmanager.types.ingress_address_list_arn_list.deserialize_aws_json_1_0(
                data["AddressLists"]
            )
        )
    else:
        raise DeserializationError("IngressIsInAddressList.address_lists required")
    return out
