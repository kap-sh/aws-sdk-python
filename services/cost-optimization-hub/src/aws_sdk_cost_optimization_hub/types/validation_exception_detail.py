"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ValidationExceptionDetail``."""

from typing import TypedDict

from aws_sdk_cost_optimization_hub.errors import DeserializationError


class ValidationExceptionDetail(TypedDict):
    field_name: "str"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "str"
    """<p>A message with the reason for the validation exception error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionDetail) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionDetail:
    out: ValidationExceptionDetail = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError("ValidationExceptionDetail.field_name required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionDetail.message required")
    return out
