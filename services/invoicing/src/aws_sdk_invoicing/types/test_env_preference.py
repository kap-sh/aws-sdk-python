"""Generated from Smithy shape ``com.amazonaws.invoicing#TestEnvPreference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string_without_space
    import aws_sdk_invoicing.types.buyer_domain
    import aws_sdk_invoicing.types.supplier_domain


class TestEnvPreference(TypedDict):
    buyer_domain: "aws_sdk_invoicing.types.buyer_domain.BuyerDomain"
    """<p>The domain identifier for the buyer in the test environment of the procurement portal.</p>"""
    buyer_identifier: (
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the buyer in the test environment of the procurement portal.</p>"""
    supplier_domain: "aws_sdk_invoicing.types.supplier_domain.SupplierDomain"
    """<p>The domain identifier for the supplier in the test environment of the procurement portal.</p>"""
    supplier_identifier: (
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    )
    """<p>The unique identifier for the supplier in the test environment of the procurement portal.</p>"""
    procurement_portal_shared_secret: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The shared secret or authentication credential used for secure communication with the test environment.</p>"""
    procurement_portal_instance_endpoint: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL where e-invoices are delivered in the test environment.</p>"""
    purchase_order_retrieval_endpoint: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The endpoint URL used for retrieving purchase orders in the test environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestEnvPreference) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_0(data: dict) -> TestEnvPreference:
    out: TestEnvPreference = {}  # type: ignore[typeddict-item]
    if "BuyerDomain" in data:
        import aws_sdk_invoicing.types.buyer_domain

        out["buyer_domain"] = (
            aws_sdk_invoicing.types.buyer_domain.deserialize_aws_json_1_0(
                data["BuyerDomain"]
            )
        )
    else:
        raise DeserializationError("TestEnvPreference.buyer_domain required")
    if "BuyerIdentifier" in data:
        out["buyer_identifier"] = data["BuyerIdentifier"]
    else:
        raise DeserializationError("TestEnvPreference.buyer_identifier required")
    if "SupplierDomain" in data:
        import aws_sdk_invoicing.types.supplier_domain

        out["supplier_domain"] = (
            aws_sdk_invoicing.types.supplier_domain.deserialize_aws_json_1_0(
                data["SupplierDomain"]
            )
        )
    else:
        raise DeserializationError("TestEnvPreference.supplier_domain required")
    if "SupplierIdentifier" in data:
        out["supplier_identifier"] = data["SupplierIdentifier"]
    else:
        raise DeserializationError("TestEnvPreference.supplier_identifier required")
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
    return out
