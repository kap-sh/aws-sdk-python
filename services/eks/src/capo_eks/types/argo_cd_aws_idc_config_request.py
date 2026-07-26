"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdAwsIdcConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.string


class ArgoCdAwsIdcConfigRequest(TypedDict, closed=True):
    idc_instance_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity CenterIAM; Identity Center instance to use for authentication.</p>"""
    idc_region: NotRequired["capo_eks.types.string.String"]
    """<p>The Region where your IAM Identity CenterIAM; Identity Center instance is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdAwsIdcConfigRequest) -> dict:
    out: dict = {}
    out["idcInstanceArn"] = value["idc_instance_arn"]
    if "idc_region" in value:
        out["idcRegion"] = value["idc_region"]
    return out


def deserialize_json(data: dict) -> ArgoCdAwsIdcConfigRequest:
    out: ArgoCdAwsIdcConfigRequest = {}  # type: ignore[typeddict-item]
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    else:
        raise DeserializationError(
            "ArgoCdAwsIdcConfigRequest.idc_instance_arn required"
        )
    if "idcRegion" in data:
        out["idc_region"] = data["idcRegion"]
    return out
