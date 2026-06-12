"""Generated from Smithy shape ``com.amazonaws.snowball#CreateReturnShippingLabelResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.shipping_label_status


class CreateReturnShippingLabelResult(TypedDict):
    status: NotRequired[
        "aws_sdk_snowball.types.shipping_label_status.ShippingLabelStatus"
    ]
    """<p>The status information of the task on a Snow device that is being returned to Amazon Web Services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReturnShippingLabelResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_snowball.types.shipping_label_status

        out["Status"] = (
            aws_sdk_snowball.types.shipping_label_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReturnShippingLabelResult:
    out: CreateReturnShippingLabelResult = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_snowball.types.shipping_label_status

        out["status"] = (
            aws_sdk_snowball.types.shipping_label_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
