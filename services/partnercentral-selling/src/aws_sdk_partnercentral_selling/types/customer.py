"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Customer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.account
    import aws_sdk_partnercentral_selling.types.customer_contacts_list


class Customer(TypedDict):
    account: NotRequired["aws_sdk_partnercentral_selling.types.account.Account"]
    """<p>An object that contains the customer's account details.</p>"""
    contacts: NotRequired[
        "aws_sdk_partnercentral_selling.types.customer_contacts_list.CustomerContactsList"
    ]
    """<p>Represents the contact details for individuals associated with the customer of the <code>Opportunity</code>. This field captures relevant contacts, including decision-makers, influencers, and technical stakeholders within the customer organization. These contacts are key to progressing the opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Customer) -> dict:
    out: dict = {}
    if "account" in value:
        import aws_sdk_partnercentral_selling.types.account

        out["Account"] = (
            aws_sdk_partnercentral_selling.types.account.serialize_aws_json_1_0(
                value["account"]
            )
        )
    if "contacts" in value:
        import aws_sdk_partnercentral_selling.types.customer_contacts_list

        out["Contacts"] = (
            aws_sdk_partnercentral_selling.types.customer_contacts_list.serialize_aws_json_1_0(
                value["contacts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Customer:
    out: Customer = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        import aws_sdk_partnercentral_selling.types.account

        out["account"] = (
            aws_sdk_partnercentral_selling.types.account.deserialize_aws_json_1_0(
                data["Account"]
            )
        )
    if "Contacts" in data:
        import aws_sdk_partnercentral_selling.types.customer_contacts_list

        out["contacts"] = (
            aws_sdk_partnercentral_selling.types.customer_contacts_list.deserialize_aws_json_1_0(
                data["Contacts"]
            )
        )
    return out
