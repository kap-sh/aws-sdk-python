"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisionedProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.record_detail


class UpdateProvisionedProductOutput(TypedDict, closed=True):
    record_detail: NotRequired[
        "aws_sdk_service_catalog.types.record_detail.RecordDetail"
    ]
    """<p>Information about the result of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedProductOutput) -> dict:
    out: dict = {}
    if "record_detail" in value:
        import aws_sdk_service_catalog.types.record_detail

        out["RecordDetail"] = (
            aws_sdk_service_catalog.types.record_detail.serialize_aws_json_1_1(
                value["record_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedProductOutput:
    out: UpdateProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if "RecordDetail" in data:
        import aws_sdk_service_catalog.types.record_detail

        out["record_detail"] = (
            aws_sdk_service_catalog.types.record_detail.deserialize_aws_json_1_1(
                data["RecordDetail"]
            )
        )
    return out
