"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DeleteHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.cluster_id
    import aws_sdk_cloudhsm_v2.types.eni_id
    import aws_sdk_cloudhsm_v2.types.hsm_id
    import aws_sdk_cloudhsm_v2.types.ip_address


class DeleteHsmRequest(TypedDict, closed=True):
    cluster_id: "aws_sdk_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the cluster that contains the HSM that you are deleting.</p>"""
    hsm_id: NotRequired["aws_sdk_cloudhsm_v2.types.hsm_id.HsmId"]
    """<p>The identifier (ID) of the HSM that you are deleting.</p>"""
    eni_id: NotRequired["aws_sdk_cloudhsm_v2.types.eni_id.EniId"]
    """<p>The identifier (ID) of the elastic network interface (ENI) of the HSM that you are deleting.</p>"""
    eni_ip: NotRequired["aws_sdk_cloudhsm_v2.types.ip_address.IpAddress"]
    """<p>The IP address of the elastic network interface (ENI) of the HSM that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHsmRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    if "hsm_id" in value:
        out["HsmId"] = value["hsm_id"]
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHsmRequest:
    out: DeleteHsmRequest = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    else:
        raise DeserializationError("DeleteHsmRequest.cluster_id required")
    if "HsmId" in data:
        out["hsm_id"] = data["HsmId"]
    if "EniId" in data:
        out["eni_id"] = data["EniId"]
    if "EniIp" in data:
        out["eni_ip"] = data["EniIp"]
    return out
