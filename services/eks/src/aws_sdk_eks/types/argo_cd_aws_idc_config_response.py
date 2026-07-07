"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdAwsIdcConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class ArgoCdAwsIdcConfigResponse(TypedDict, closed=True):
    idc_instance_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity CenterIAM; Identity Center instance used for authentication.</p>"""
    idc_region: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Region where the IAM Identity CenterIAM; Identity Center instance is located.</p>"""
    idc_managed_application_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the managed application created in IAM Identity CenterIAM; Identity Center for this Argo CD capability. This application is automatically created and managed by Amazon EKS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdAwsIdcConfigResponse) -> dict:
    out: dict = {}
    if "idc_instance_arn" in value:
        out["idcInstanceArn"] = value["idc_instance_arn"]
    if "idc_region" in value:
        out["idcRegion"] = value["idc_region"]
    if "idc_managed_application_arn" in value:
        out["idcManagedApplicationArn"] = value["idc_managed_application_arn"]
    return out


def deserialize_json(data: dict) -> ArgoCdAwsIdcConfigResponse:
    out: ArgoCdAwsIdcConfigResponse = {}  # type: ignore[typeddict-item]
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    if "idcRegion" in data:
        out["idc_region"] = data["idcRegion"]
    if "idcManagedApplicationArn" in data:
        out["idc_managed_application_arn"] = data["idcManagedApplicationArn"]
    return out
