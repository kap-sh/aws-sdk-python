"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_invoicing.types.account_id_string
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.basic_string_without_space
    import aws_sdk_invoicing.types.buyer_domain
    import aws_sdk_invoicing.types.contacts
    import aws_sdk_invoicing.types.einvoice_delivery_preference
    import aws_sdk_invoicing.types.procurement_portal_name
    import aws_sdk_invoicing.types.procurement_portal_preference_arn_string
    import aws_sdk_invoicing.types.procurement_portal_preference_selector
    import aws_sdk_invoicing.types.procurement_portal_preference_status
    import aws_sdk_invoicing.types.supplier_domain
    import aws_sdk_invoicing.types.test_env_preference


class ProcurementPortalPreference(TypedDict, closed=True):
    aws_account_id: "aws_sdk_invoicing.types.account_id_string.AccountIdString"
    """<p>The Amazon Web Services account ID associated with this procurement portal preference.</p>"""
    procurement_portal_preference_arn: "aws_sdk_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference.</p>"""
    procurement_portal_name: (
        "aws_sdk_invoicing.types.procurement_portal_name.ProcurementPortalName"
    )
    """<p>The name of the procurement portal.</p>"""
    buyer_domain: "aws_sdk_invoicing.types.buyer_domain.BuyerDomain"
    """<p>The domain identifier for the buyer in the procurement portal.</p>"""
    buyer_identifier: (
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the buyer in the procurement portal.</p>"""
    supplier_domain: "aws_sdk_invoicing.types.supplier_domain.SupplierDomain"
    """<p>The domain identifier for the supplier in the procurement portal.</p>"""
    supplier_identifier: (
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the supplier in the procurement portal.</p>"""
    selector: NotRequired[
        "aws_sdk_invoicing.types.procurement_portal_preference_selector.ProcurementPortalPreferenceSelector"
    ]
    procurement_portal_shared_secret: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The shared secret or authentication credential used for secure communication with the procurement portal.</p>"""
    procurement_portal_instance_endpoint: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL where e-invoices are delivered to the procurement portal.</p>"""
    purchase_order_retrieval_endpoint: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL used for retrieving purchase orders from the procurement portal.</p>"""
    test_env_preference: NotRequired[
        "aws_sdk_invoicing.types.test_env_preference.TestEnvPreference"
    ]
    """<p>Configuration on settings for the test environment of the procurement portal.</p>"""
    einvoice_delivery_enabled: "bool"
    """<p>Indicates whether e-invoice delivery is enabled for this procurement portal preference.</p>"""
    einvoice_delivery_preference: NotRequired[
        "aws_sdk_invoicing.types.einvoice_delivery_preference.EinvoiceDeliveryPreference"
    ]
    """<p>The configuration settings that specify how e-invoices are delivered to the procurement portal.</p>"""
    purchase_order_retrieval_enabled: "bool"
    """<p>Indicates whether purchase order retrieval is enabled for this procurement portal preference.</p>"""
    contacts: NotRequired["aws_sdk_invoicing.types.contacts.Contacts"]
    """<p>List of contact information for portal administrators and technical contacts.</p>"""
    einvoice_delivery_preference_status: NotRequired[
        "aws_sdk_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
    ]
    """<p>The current status of the e-invoice delivery preference.</p>"""
    einvoice_delivery_preference_status_reason: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p>The reason for the current e-invoice delivery preference status.</p>"""
    purchase_order_retrieval_preference_status: NotRequired[
        "aws_sdk_invoicing.types.procurement_portal_preference_status.ProcurementPortalPreferenceStatus"
    ]
    """<p>The current status of the purchase order retrieval preference.</p>"""
    purchase_order_retrieval_preference_status_reason: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p>The reason for the current purchase order retrieval preference status.</p>"""
    version: "int"
    """<p>The version number of the procurement portal preference configuration.</p>"""
    create_date: "datetime.datetime"
    """<p>The date and time when the procurement portal preference was created.</p>"""
    last_update_date: "datetime.datetime"
    """<p>The date and time when the procurement portal preference was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalPreference) -> dict:
    out: dict = {}
    out["AwsAccountId"] = value["aws_account_id"]
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    import aws_sdk_invoicing.types.procurement_portal_name

    out["ProcurementPortalName"] = (
        aws_sdk_invoicing.types.procurement_portal_name.serialize_aws_json_1_0(
            value["procurement_portal_name"]
        )
    )
    import aws_sdk_invoicing.types.buyer_domain

    out["BuyerDomain"] = aws_sdk_invoicing.types.buyer_domain.serialize_aws_json_1_0(
        value["buyer_domain"]
    )
    out["BuyerIdentifier"] = value["buyer_identifier"]
    import aws_sdk_invoicing.types.supplier_domain

    out["SupplierDomain"] = (
        aws_sdk_invoicing.types.supplier_domain.serialize_aws_json_1_0(
            value["supplier_domain"]
        )
    )
    out["SupplierIdentifier"] = value["supplier_identifier"]
    if "selector" in value:
        import aws_sdk_invoicing.types.procurement_portal_preference_selector

        out["Selector"] = (
            aws_sdk_invoicing.types.procurement_portal_preference_selector.serialize_aws_json_1_0(
                value["selector"]
            )
        )
    if "procurement_portal_shared_secret" in value:
        out["ProcurementPortalSharedSecret"] = value["procurement_portal_shared_secret"]
    if "procurement_portal_instance_endpoint" in value:
        out["ProcurementPortalInstanceEndpoint"] = value[
            "procurement_portal_instance_endpoint"
        ]
    if "purchase_order_retrieval_endpoint" in value:
        out["PurchaseOrderRetrievalEndpoint"] = value[
            "purchase_order_retrieval_endpoint"
        ]
    if "test_env_preference" in value:
        import aws_sdk_invoicing.types.test_env_preference

        out["TestEnvPreference"] = (
            aws_sdk_invoicing.types.test_env_preference.serialize_aws_json_1_0(
                value["test_env_preference"]
            )
        )
    out["EinvoiceDeliveryEnabled"] = value["einvoice_delivery_enabled"]
    if "einvoice_delivery_preference" in value:
        import aws_sdk_invoicing.types.einvoice_delivery_preference

        out["EinvoiceDeliveryPreference"] = (
            aws_sdk_invoicing.types.einvoice_delivery_preference.serialize_aws_json_1_0(
                value["einvoice_delivery_preference"]
            )
        )
    out["PurchaseOrderRetrievalEnabled"] = value["purchase_order_retrieval_enabled"]
    if "contacts" in value:
        import aws_sdk_invoicing.types.contacts

        out["Contacts"] = aws_sdk_invoicing.types.contacts.serialize_aws_json_1_0(
            value["contacts"]
        )
    if "einvoice_delivery_preference_status" in value:
        import aws_sdk_invoicing.types.procurement_portal_preference_status

        out["EinvoiceDeliveryPreferenceStatus"] = (
            aws_sdk_invoicing.types.procurement_portal_preference_status.serialize_aws_json_1_0(
                value["einvoice_delivery_preference_status"]
            )
        )
    if "einvoice_delivery_preference_status_reason" in value:
        out["EinvoiceDeliveryPreferenceStatusReason"] = value[
            "einvoice_delivery_preference_status_reason"
        ]
    if "purchase_order_retrieval_preference_status" in value:
        import aws_sdk_invoicing.types.procurement_portal_preference_status

        out["PurchaseOrderRetrievalPreferenceStatus"] = (
            aws_sdk_invoicing.types.procurement_portal_preference_status.serialize_aws_json_1_0(
                value["purchase_order_retrieval_preference_status"]
            )
        )
    if "purchase_order_retrieval_preference_status_reason" in value:
        out["PurchaseOrderRetrievalPreferenceStatusReason"] = value[
            "purchase_order_retrieval_preference_status_reason"
        ]
    out["Version"] = value["version"]
    import aws_sdk_invoicing.types._prelude.timestamp

    out["CreateDate"] = (
        aws_sdk_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["create_date"]
        )
    )
    import aws_sdk_invoicing.types._prelude.timestamp

    out["LastUpdateDate"] = (
        aws_sdk_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_update_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProcurementPortalPreference:
    out: ProcurementPortalPreference = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.aws_account_id required"
        )
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.procurement_portal_preference_arn required"
        )
    if "ProcurementPortalName" in data:
        import aws_sdk_invoicing.types.procurement_portal_name

        out["procurement_portal_name"] = (
            aws_sdk_invoicing.types.procurement_portal_name.deserialize_aws_json_1_0(
                data["ProcurementPortalName"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.procurement_portal_name required"
        )
    if "BuyerDomain" in data:
        import aws_sdk_invoicing.types.buyer_domain

        out["buyer_domain"] = (
            aws_sdk_invoicing.types.buyer_domain.deserialize_aws_json_1_0(
                data["BuyerDomain"]
            )
        )
    else:
        raise DeserializationError("ProcurementPortalPreference.buyer_domain required")
    if "BuyerIdentifier" in data:
        out["buyer_identifier"] = data["BuyerIdentifier"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.buyer_identifier required"
        )
    if "SupplierDomain" in data:
        import aws_sdk_invoicing.types.supplier_domain

        out["supplier_domain"] = (
            aws_sdk_invoicing.types.supplier_domain.deserialize_aws_json_1_0(
                data["SupplierDomain"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.supplier_domain required"
        )
    if "SupplierIdentifier" in data:
        out["supplier_identifier"] = data["SupplierIdentifier"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.supplier_identifier required"
        )
    if "Selector" in data:
        import aws_sdk_invoicing.types.procurement_portal_preference_selector

        out["selector"] = (
            aws_sdk_invoicing.types.procurement_portal_preference_selector.deserialize_aws_json_1_0(
                data["Selector"]
            )
        )
    if "ProcurementPortalSharedSecret" in data:
        out["procurement_portal_shared_secret"] = data["ProcurementPortalSharedSecret"]
    if "ProcurementPortalInstanceEndpoint" in data:
        out["procurement_portal_instance_endpoint"] = data[
            "ProcurementPortalInstanceEndpoint"
        ]
    if "PurchaseOrderRetrievalEndpoint" in data:
        out["purchase_order_retrieval_endpoint"] = data[
            "PurchaseOrderRetrievalEndpoint"
        ]
    if "TestEnvPreference" in data:
        import aws_sdk_invoicing.types.test_env_preference

        out["test_env_preference"] = (
            aws_sdk_invoicing.types.test_env_preference.deserialize_aws_json_1_0(
                data["TestEnvPreference"]
            )
        )
    if "EinvoiceDeliveryEnabled" in data:
        out["einvoice_delivery_enabled"] = data["EinvoiceDeliveryEnabled"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.einvoice_delivery_enabled required"
        )
    if "EinvoiceDeliveryPreference" in data:
        import aws_sdk_invoicing.types.einvoice_delivery_preference

        out["einvoice_delivery_preference"] = (
            aws_sdk_invoicing.types.einvoice_delivery_preference.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryPreference"]
            )
        )
    if "PurchaseOrderRetrievalEnabled" in data:
        out["purchase_order_retrieval_enabled"] = data["PurchaseOrderRetrievalEnabled"]
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.purchase_order_retrieval_enabled required"
        )
    if "Contacts" in data:
        import aws_sdk_invoicing.types.contacts

        out["contacts"] = aws_sdk_invoicing.types.contacts.deserialize_aws_json_1_0(
            data["Contacts"]
        )
    if "EinvoiceDeliveryPreferenceStatus" in data:
        import aws_sdk_invoicing.types.procurement_portal_preference_status

        out["einvoice_delivery_preference_status"] = (
            aws_sdk_invoicing.types.procurement_portal_preference_status.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryPreferenceStatus"]
            )
        )
    if "EinvoiceDeliveryPreferenceStatusReason" in data:
        out["einvoice_delivery_preference_status_reason"] = data[
            "EinvoiceDeliveryPreferenceStatusReason"
        ]
    if "PurchaseOrderRetrievalPreferenceStatus" in data:
        import aws_sdk_invoicing.types.procurement_portal_preference_status

        out["purchase_order_retrieval_preference_status"] = (
            aws_sdk_invoicing.types.procurement_portal_preference_status.deserialize_aws_json_1_0(
                data["PurchaseOrderRetrievalPreferenceStatus"]
            )
        )
    if "PurchaseOrderRetrievalPreferenceStatusReason" in data:
        out["purchase_order_retrieval_preference_status_reason"] = data[
            "PurchaseOrderRetrievalPreferenceStatusReason"
        ]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("ProcurementPortalPreference.version required")
    if "CreateDate" in data:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["create_date"] = (
            aws_sdk_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreateDate"]
            )
        )
    else:
        raise DeserializationError("ProcurementPortalPreference.create_date required")
    if "LastUpdateDate" in data:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["last_update_date"] = (
            aws_sdk_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "ProcurementPortalPreference.last_update_date required"
        )
    return out
