"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkServiceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_info_id


class UpdateSolNetworkServiceData(TypedDict, closed=True):
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor.</p>"""
    additional_params_for_ns: NotRequired["object"]
    """<p>Values for the configurable properties declared in the network service descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkServiceData) -> dict:
    out: dict = {}
    out["nsdInfoId"] = value["nsd_info_id"]
    if "additional_params_for_ns" in value:
        out["additionalParamsForNs"] = value["additional_params_for_ns"]
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkServiceData:
    out: UpdateSolNetworkServiceData = {}  # type: ignore[typeddict-item]
    if "nsdInfoId" in data:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        raise DeserializationError("UpdateSolNetworkServiceData.nsd_info_id required")
    if "additionalParamsForNs" in data:
        out["additional_params_for_ns"] = data["additionalParamsForNs"]
    return out
