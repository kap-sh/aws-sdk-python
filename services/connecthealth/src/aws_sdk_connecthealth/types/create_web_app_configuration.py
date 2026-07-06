"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateWebAppConfiguration``."""

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError


class CreateWebAppConfiguration(TypedDict, closed=True):
    ehr_role: "str"
    """<p>ARN of the IAM role used for EHR operations.</p>"""
    idc_instance_id: "str"
    """<p>The Identity Center instance ID to use for creating the application.</p>"""
    idc_region: "str"
    """<p>The AWS region where Identity Center is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebAppConfiguration) -> dict:
    out: dict = {}
    out["ehrRole"] = value["ehr_role"]
    out["idcInstanceId"] = value["idc_instance_id"]
    out["idcRegion"] = value["idc_region"]
    return out


def deserialize_json(data: dict) -> CreateWebAppConfiguration:
    out: CreateWebAppConfiguration = {}  # type: ignore[typeddict-item]
    if "ehrRole" in data:
        out["ehr_role"] = data["ehrRole"]
    else:
        raise DeserializationError("CreateWebAppConfiguration.ehr_role required")
    if "idcInstanceId" in data:
        out["idc_instance_id"] = data["idcInstanceId"]
    else:
        raise DeserializationError("CreateWebAppConfiguration.idc_instance_id required")
    if "idcRegion" in data:
        out["idc_region"] = data["idcRegion"]
    else:
        raise DeserializationError("CreateWebAppConfiguration.idc_region required")
    return out
