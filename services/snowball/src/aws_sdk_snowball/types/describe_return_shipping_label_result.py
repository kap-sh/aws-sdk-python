"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeReturnShippingLabelResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.shipping_label_status
    import aws_sdk_snowball.types.string
    import aws_sdk_snowball.types.timestamp


class DescribeReturnShippingLabelResult(TypedDict):
    status: NotRequired[
        "aws_sdk_snowball.types.shipping_label_status.ShippingLabelStatus"
    ]
    """<p>The status information of the task on a Snow device that is being returned to Amazon Web Services.</p>"""
    expiration_date: NotRequired["aws_sdk_snowball.types.timestamp.Timestamp"]
    """<p>The expiration date of the current return shipping label.</p>"""
    return_shipping_label_uri: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The pre-signed Amazon S3 URI used to download the return shipping label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReturnShippingLabelResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_snowball.types.shipping_label_status

        out["Status"] = (
            aws_sdk_snowball.types.shipping_label_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "expiration_date" in value:
        import aws_sdk_snowball.types.timestamp

        out["ExpirationDate"] = aws_sdk_snowball.types.timestamp.serialize_aws_json_1_1(
            value["expiration_date"]
        )
    if "return_shipping_label_uri" in value:
        out["ReturnShippingLabelURI"] = value["return_shipping_label_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReturnShippingLabelResult:
    out: DescribeReturnShippingLabelResult = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_snowball.types.shipping_label_status

        out["status"] = (
            aws_sdk_snowball.types.shipping_label_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ExpirationDate" in data:
        import aws_sdk_snowball.types.timestamp

        out["expiration_date"] = (
            aws_sdk_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationDate"]
            )
        )
    if "ReturnShippingLabelURI" in data:
        out["return_shipping_label_uri"] = data["ReturnShippingLabelURI"]
    return out
