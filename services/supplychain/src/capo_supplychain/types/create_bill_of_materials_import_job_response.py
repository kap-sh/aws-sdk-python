"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateBillOfMaterialsImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.uuid


class CreateBillOfMaterialsImportJobResponse(TypedDict, closed=True):
    job_id: "capo_supplychain.types.uuid.UUID"
    """<p>The new BillOfMaterialsImportJob identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBillOfMaterialsImportJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateBillOfMaterialsImportJobResponse:
    out: CreateBillOfMaterialsImportJobResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError(
            "CreateBillOfMaterialsImportJobResponse.job_id required"
        )
    return out
