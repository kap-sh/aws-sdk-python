"""Generated from Smithy shape ``com.amazonaws.invoicing#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.billing_entity


class Entity(TypedDict, closed=True):
    invoicing_entity: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The name of the entity that issues the Amazon Web Services invoice.</p>"""
    billing_entity: NotRequired["aws_sdk_invoicing.types.billing_entity.BillingEntity"]
    """<p>Helps you identify whether your invoices are for Amazon Web Services Marketplace or for purchases of other Amazon Web Services services.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Entity) -> dict:
    out: dict = {}
    if "invoicing_entity" in value:
        out["InvoicingEntity"] = value["invoicing_entity"]
    if "billing_entity" in value:
        import aws_sdk_invoicing.types.billing_entity

        out["BillingEntity"] = (
            aws_sdk_invoicing.types.billing_entity.serialize_aws_json_1_0(
                value["billing_entity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "InvoicingEntity" in data:
        out["invoicing_entity"] = data["InvoicingEntity"]
    if "BillingEntity" in data:
        import aws_sdk_invoicing.types.billing_entity

        out["billing_entity"] = (
            aws_sdk_invoicing.types.billing_entity.deserialize_aws_json_1_0(
                data["BillingEntity"]
            )
        )
    return out
