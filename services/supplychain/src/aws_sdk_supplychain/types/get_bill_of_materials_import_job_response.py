"""Generated from Smithy shape ``com.amazonaws.supplychain#GetBillOfMaterialsImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.bill_of_materials_import_job


class GetBillOfMaterialsImportJobResponse(TypedDict, closed=True):
    job: "aws_sdk_supplychain.types.bill_of_materials_import_job.BillOfMaterialsImportJob"
    """<p>The BillOfMaterialsImportJob.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBillOfMaterialsImportJobResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.bill_of_materials_import_job

    out["job"] = aws_sdk_supplychain.types.bill_of_materials_import_job.serialize_json(
        value["job"]
    )
    return out


def deserialize_json(data: dict) -> GetBillOfMaterialsImportJobResponse:
    out: GetBillOfMaterialsImportJobResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_supplychain.types.bill_of_materials_import_job

        out["job"] = (
            aws_sdk_supplychain.types.bill_of_materials_import_job.deserialize_json(
                data["job"]
            )
        )
    else:
        raise DeserializationError("GetBillOfMaterialsImportJobResponse.job required")
    return out
