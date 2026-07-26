"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataAccessorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor_arn
    import capo_qbusiness.types.data_accessor_id
    import capo_qbusiness.types.idc_application_arn


class CreateDataAccessorResponse(TypedDict, closed=True):
    data_accessor_id: "capo_qbusiness.types.data_accessor_id.DataAccessorId"
    """<p>The unique identifier of the created data accessor.</p>"""
    idc_application_arn: "capo_qbusiness.types.idc_application_arn.IdcApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application created for this data accessor.</p>"""
    data_accessor_arn: "capo_qbusiness.types.data_accessor_arn.DataAccessorArn"
    """<p>The Amazon Resource Name (ARN) of the created data accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAccessorResponse) -> dict:
    out: dict = {}
    out["dataAccessorId"] = value["data_accessor_id"]
    out["idcApplicationArn"] = value["idc_application_arn"]
    out["dataAccessorArn"] = value["data_accessor_arn"]
    return out


def deserialize_json(data: dict) -> CreateDataAccessorResponse:
    out: CreateDataAccessorResponse = {}  # type: ignore[typeddict-item]
    if "dataAccessorId" in data:
        out["data_accessor_id"] = data["dataAccessorId"]
    else:
        raise DeserializationError(
            "CreateDataAccessorResponse.data_accessor_id required"
        )
    if "idcApplicationArn" in data:
        out["idc_application_arn"] = data["idcApplicationArn"]
    else:
        raise DeserializationError(
            "CreateDataAccessorResponse.idc_application_arn required"
        )
    if "dataAccessorArn" in data:
        out["data_accessor_arn"] = data["dataAccessorArn"]
    else:
        raise DeserializationError(
            "CreateDataAccessorResponse.data_accessor_arn required"
        )
    return out
