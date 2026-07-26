"""Generated from Smithy shape ``com.amazonaws.invoicing#PutProcurementPortalPreferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.contacts
    import capo_invoicing.types.einvoice_delivery_preference
    import capo_invoicing.types.procurement_portal_preference_arn_string
    import capo_invoicing.types.procurement_portal_preference_selector
    import capo_invoicing.types.sensitive_basic_string_without_space
    import capo_invoicing.types.test_env_preference_input


class PutProcurementPortalPreferenceRequest(TypedDict, closed=True):
    procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference to update.</p>"""
    selector: NotRequired[
        "capo_invoicing.types.procurement_portal_preference_selector.ProcurementPortalPreferenceSelector"
    ]
    procurement_portal_shared_secret: NotRequired[
        "capo_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
    ]
    """<p>The updated shared secret or authentication credential for the procurement portal. This value must be encrypted at rest.</p>"""
    procurement_portal_instance_endpoint: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The updated endpoint URL where e-invoices will be delivered to the procurement portal. Must be a valid HTTPS URL.</p>"""
    test_env_preference: NotRequired[
        "capo_invoicing.types.test_env_preference_input.TestEnvPreferenceInput"
    ]
    """<p>Updated configuration settings for the test environment of the procurement portal.</p>"""
    einvoice_delivery_enabled: "bool"
    """<p>Updated flag indicating whether e-invoice delivery is enabled for this procurement portal preference.</p>"""
    einvoice_delivery_preference: NotRequired[
        "capo_invoicing.types.einvoice_delivery_preference.EinvoiceDeliveryPreference"
    ]
    """<p>Updated e-invoice delivery configuration including document types, attachment types, and customization settings for the portal.</p>"""
    purchase_order_retrieval_enabled: "bool"
    """<p>Updated flag indicating whether purchase order retrieval is enabled for this procurement portal preference.</p>"""
    contacts: "capo_invoicing.types.contacts.Contacts"
    """<p>Updated list of contact information for portal administrators and technical contacts.</p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutProcurementPortalPreferenceRequest) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    if "selector" in value:
        import capo_invoicing.types.procurement_portal_preference_selector

        out["Selector"] = (
            capo_invoicing.types.procurement_portal_preference_selector.serialize_aws_json_1_0(
                value["selector"]
            )
        )
    if "procurement_portal_shared_secret" in value:
        out["ProcurementPortalSharedSecret"] = value["procurement_portal_shared_secret"]
    if "procurement_portal_instance_endpoint" in value:
        out["ProcurementPortalInstanceEndpoint"] = value[
            "procurement_portal_instance_endpoint"
        ]
    if "test_env_preference" in value:
        import capo_invoicing.types.test_env_preference_input

        out["TestEnvPreference"] = (
            capo_invoicing.types.test_env_preference_input.serialize_aws_json_1_0(
                value["test_env_preference"]
            )
        )
    out["EinvoiceDeliveryEnabled"] = value["einvoice_delivery_enabled"]
    if "einvoice_delivery_preference" in value:
        import capo_invoicing.types.einvoice_delivery_preference

        out["EinvoiceDeliveryPreference"] = (
            capo_invoicing.types.einvoice_delivery_preference.serialize_aws_json_1_0(
                value["einvoice_delivery_preference"]
            )
        )
    out["PurchaseOrderRetrievalEnabled"] = value["purchase_order_retrieval_enabled"]
    import capo_invoicing.types.contacts

    out["Contacts"] = capo_invoicing.types.contacts.serialize_aws_json_1_0(
        value["contacts"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutProcurementPortalPreferenceRequest:
    out: PutProcurementPortalPreferenceRequest = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "PutProcurementPortalPreferenceRequest.procurement_portal_preference_arn required"
        )
    if "Selector" in data:
        import capo_invoicing.types.procurement_portal_preference_selector

        out["selector"] = (
            capo_invoicing.types.procurement_portal_preference_selector.deserialize_aws_json_1_0(
                data["Selector"]
            )
        )
    if "ProcurementPortalSharedSecret" in data:
        out["procurement_portal_shared_secret"] = data["ProcurementPortalSharedSecret"]
    if "ProcurementPortalInstanceEndpoint" in data:
        out["procurement_portal_instance_endpoint"] = data[
            "ProcurementPortalInstanceEndpoint"
        ]
    if "TestEnvPreference" in data:
        import capo_invoicing.types.test_env_preference_input

        out["test_env_preference"] = (
            capo_invoicing.types.test_env_preference_input.deserialize_aws_json_1_0(
                data["TestEnvPreference"]
            )
        )
    if "EinvoiceDeliveryEnabled" in data:
        out["einvoice_delivery_enabled"] = data["EinvoiceDeliveryEnabled"]
    else:
        raise DeserializationError(
            "PutProcurementPortalPreferenceRequest.einvoice_delivery_enabled required"
        )
    if "EinvoiceDeliveryPreference" in data:
        import capo_invoicing.types.einvoice_delivery_preference

        out["einvoice_delivery_preference"] = (
            capo_invoicing.types.einvoice_delivery_preference.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryPreference"]
            )
        )
    if "PurchaseOrderRetrievalEnabled" in data:
        out["purchase_order_retrieval_enabled"] = data["PurchaseOrderRetrievalEnabled"]
    else:
        raise DeserializationError(
            "PutProcurementPortalPreferenceRequest.purchase_order_retrieval_enabled required"
        )
    if "Contacts" in data:
        import capo_invoicing.types.contacts

        out["contacts"] = capo_invoicing.types.contacts.deserialize_aws_json_1_0(
            data["Contacts"]
        )
    else:
        raise DeserializationError(
            "PutProcurementPortalPreferenceRequest.contacts required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
