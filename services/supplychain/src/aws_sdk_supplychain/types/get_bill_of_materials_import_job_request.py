"""Generated from Smithy shape ``com.amazonaws.supplychain#GetBillOfMaterialsImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.uuid


class GetBillOfMaterialsImportJobRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    job_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The BillOfMaterialsImportJob identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBillOfMaterialsImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBillOfMaterialsImportJobRequest:
    out: GetBillOfMaterialsImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
