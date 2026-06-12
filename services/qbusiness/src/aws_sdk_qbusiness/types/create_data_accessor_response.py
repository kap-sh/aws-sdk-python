"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataAccessorResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_accessor_arn
    import aws_sdk_qbusiness.types.data_accessor_id
    import aws_sdk_qbusiness.types.idc_application_arn

class CreateDataAccessorResponse(TypedDict):
    data_accessor_id: "aws_sdk_qbusiness.types.data_accessor_id.DataAccessorId"
    """<p>The unique identifier of the created data accessor.</p>"""
    idc_application_arn: "aws_sdk_qbusiness.types.idc_application_arn.IdcApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application created for this data accessor.</p>"""
    data_accessor_arn: "aws_sdk_qbusiness.types.data_accessor_arn.DataAccessorArn"
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
        raise DeserializationError("CreateDataAccessorResponse.data_accessor_id required")
    if "idcApplicationArn" in data:
        out["idc_application_arn"] = data["idcApplicationArn"]
    else:
        raise DeserializationError("CreateDataAccessorResponse.idc_application_arn required")
    if "dataAccessorArn" in data:
        out["data_accessor_arn"] = data["dataAccessorArn"]
    else:
        raise DeserializationError("CreateDataAccessorResponse.data_accessor_arn required")
    return out