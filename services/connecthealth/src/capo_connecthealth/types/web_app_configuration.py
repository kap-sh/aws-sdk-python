"""Generated from Smithy shape ``com.amazonaws.connecthealth#WebAppConfiguration``."""

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError


class WebAppConfiguration(TypedDict, closed=True):
    ehr_role: "str"
    """<p>ARN of the IAM role used for EHR operations.</p>"""
    idc_application_id: "str"
    """<p>The Identity Center application ID associated with this Domain.</p>"""
    idc_region: "str"
    """<p>The AWS region where Identity Center is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebAppConfiguration) -> dict:
    out: dict = {}
    out["ehrRole"] = value["ehr_role"]
    out["idcApplicationId"] = value["idc_application_id"]
    out["idcRegion"] = value["idc_region"]
    return out


def deserialize_json(data: dict) -> WebAppConfiguration:
    out: WebAppConfiguration = {}  # type: ignore[typeddict-item]
    if "ehrRole" in data:
        out["ehr_role"] = data["ehrRole"]
    else:
        raise DeserializationError("WebAppConfiguration.ehr_role required")
    if "idcApplicationId" in data:
        out["idc_application_id"] = data["idcApplicationId"]
    else:
        raise DeserializationError("WebAppConfiguration.idc_application_id required")
    if "idcRegion" in data:
        out["idc_region"] = data["idcRegion"]
    else:
        raise DeserializationError("WebAppConfiguration.idc_region required")
    return out
