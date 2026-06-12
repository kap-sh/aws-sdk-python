"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisionedProductPropertiesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.provisioned_product_properties
    import aws_sdk_service_catalog.types.record_status


class UpdateProvisionedProductPropertiesOutput(TypedDict):
    provisioned_product_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The provisioned product identifier.</p>"""
    provisioned_product_properties: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_properties.ProvisionedProductProperties"
    ]
    """<p>A map that contains the properties updated.</p>"""
    record_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the record.</p>"""
    status: NotRequired["aws_sdk_service_catalog.types.record_status.RecordStatus"]
    """<p>The status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedProductPropertiesOutput) -> dict:
    out: dict = {}
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "provisioned_product_properties" in value:
        import aws_sdk_service_catalog.types.provisioned_product_properties

        out["ProvisionedProductProperties"] = (
            aws_sdk_service_catalog.types.provisioned_product_properties.serialize_aws_json_1_1(
                value["provisioned_product_properties"]
            )
        )
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "status" in value:
        import aws_sdk_service_catalog.types.record_status

        out["Status"] = (
            aws_sdk_service_catalog.types.record_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedProductPropertiesOutput:
    out: UpdateProvisionedProductPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "ProvisionedProductId" in data:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if "ProvisionedProductProperties" in data:
        import aws_sdk_service_catalog.types.provisioned_product_properties

        out["provisioned_product_properties"] = (
            aws_sdk_service_catalog.types.provisioned_product_properties.deserialize_aws_json_1_1(
                data["ProvisionedProductProperties"]
            )
        )
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    if "Status" in data:
        import aws_sdk_service_catalog.types.record_status

        out["status"] = (
            aws_sdk_service_catalog.types.record_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
