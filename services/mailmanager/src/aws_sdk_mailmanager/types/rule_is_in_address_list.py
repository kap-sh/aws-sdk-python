"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIsInAddressList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_address_list_arn_list
    import aws_sdk_mailmanager.types.rule_address_list_email_attribute


class RuleIsInAddressList(TypedDict, closed=True):
    attribute: "aws_sdk_mailmanager.types.rule_address_list_email_attribute.RuleAddressListEmailAttribute"
    """<p>The email attribute that needs to be evaluated against the address list.</p>"""
    address_lists: (
        "aws_sdk_mailmanager.types.rule_address_list_arn_list.RuleAddressListArnList"
    )
    """<p>The address lists that will be used for evaluation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIsInAddressList) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.rule_address_list_email_attribute

    out["Attribute"] = (
        aws_sdk_mailmanager.types.rule_address_list_email_attribute.serialize_aws_json_1_0(
            value["attribute"]
        )
    )
    import aws_sdk_mailmanager.types.rule_address_list_arn_list

    out["AddressLists"] = (
        aws_sdk_mailmanager.types.rule_address_list_arn_list.serialize_aws_json_1_0(
            value["address_lists"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleIsInAddressList:
    out: RuleIsInAddressList = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_mailmanager.types.rule_address_list_email_attribute

        out["attribute"] = (
            aws_sdk_mailmanager.types.rule_address_list_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        )
    else:
        raise DeserializationError("RuleIsInAddressList.attribute required")
    if "AddressLists" in data:
        import aws_sdk_mailmanager.types.rule_address_list_arn_list

        out["address_lists"] = (
            aws_sdk_mailmanager.types.rule_address_list_arn_list.deserialize_aws_json_1_0(
                data["AddressLists"]
            )
        )
    else:
        raise DeserializationError("RuleIsInAddressList.address_lists required")
    return out
