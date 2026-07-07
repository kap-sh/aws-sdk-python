"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.created_time
    import aws_sdk_service_catalog.types.product_view_summary
    import aws_sdk_service_catalog.types.resource_arn
    import aws_sdk_service_catalog.types.source_connection_detail
    import aws_sdk_service_catalog.types.status


class ProductViewDetail(TypedDict, closed=True):
    product_view_summary: NotRequired[
        "aws_sdk_service_catalog.types.product_view_summary.ProductViewSummary"
    ]
    """<p>Summary information about the product view.</p>"""
    status: NotRequired["aws_sdk_service_catalog.types.status.Status"]
    """<p>The status of the product.</p> <ul> <li> <p> <code>AVAILABLE</code> - The product is ready for use.</p> </li> <li> <p> <code>CREATING</code> - Product creation has started; the product is not ready for use.</p> </li> <li> <p> <code>FAILED</code> - An action failed.</p> </li> </ul>"""
    product_arn: NotRequired["aws_sdk_service_catalog.types.resource_arn.ResourceARN"]
    """<p>The ARN of the product.</p>"""
    created_time: NotRequired["aws_sdk_service_catalog.types.created_time.CreatedTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    source_connection: NotRequired[
        "aws_sdk_service_catalog.types.source_connection_detail.SourceConnectionDetail"
    ]
    """<p>A top level <code>ProductViewDetail</code> response containing details about the product’s connection. Service Catalog returns this field for the <code>CreateProduct</code>, <code>UpdateProduct</code>, <code>DescribeProductAsAdmin</code>, and <code>SearchProductAsAdmin</code> APIs. This response contains the same fields as the <code>ConnectionParameters</code> request, with the addition of the <code>LastSync</code> response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewDetail) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import aws_sdk_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            aws_sdk_service_catalog.types.product_view_summary.serialize_aws_json_1_1(
                value["product_view_summary"]
            )
        )
    if "status" in value:
        import aws_sdk_service_catalog.types.status

        out["Status"] = aws_sdk_service_catalog.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    if "product_arn" in value:
        out["ProductARN"] = value["product_arn"]
    if "created_time" in value:
        import aws_sdk_service_catalog.types.created_time

        out["CreatedTime"] = (
            aws_sdk_service_catalog.types.created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "source_connection" in value:
        import aws_sdk_service_catalog.types.source_connection_detail

        out["SourceConnection"] = (
            aws_sdk_service_catalog.types.source_connection_detail.serialize_aws_json_1_1(
                value["source_connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductViewDetail:
    out: ProductViewDetail = {}  # type: ignore[typeddict-item]
    if "ProductViewSummary" in data:
        import aws_sdk_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            aws_sdk_service_catalog.types.product_view_summary.deserialize_aws_json_1_1(
                data["ProductViewSummary"]
            )
        )
    if "Status" in data:
        import aws_sdk_service_catalog.types.status

        out["status"] = aws_sdk_service_catalog.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ProductARN" in data:
        out["product_arn"] = data["ProductARN"]
    if "CreatedTime" in data:
        import aws_sdk_service_catalog.types.created_time

        out["created_time"] = (
            aws_sdk_service_catalog.types.created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if "SourceConnection" in data:
        import aws_sdk_service_catalog.types.source_connection_detail

        out["source_connection"] = (
            aws_sdk_service_catalog.types.source_connection_detail.deserialize_aws_json_1_1(
                data["SourceConnection"]
            )
        )
    return out
