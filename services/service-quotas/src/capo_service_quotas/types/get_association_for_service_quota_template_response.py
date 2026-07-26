"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetAssociationForServiceQuotaTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.service_quota_template_association_status


class GetAssociationForServiceQuotaTemplateResponse(TypedDict, closed=True):
    service_quota_template_association_status: NotRequired[
        "capo_service_quotas.types.service_quota_template_association_status.ServiceQuotaTemplateAssociationStatus"
    ]
    """<p>The association status. If the status is <code>ASSOCIATED</code>, the quota increase requests in the template are automatically applied to new Amazon Web Services accounts in your organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAssociationForServiceQuotaTemplateResponse,
) -> dict:
    out: dict = {}
    if "service_quota_template_association_status" in value:
        import capo_service_quotas.types.service_quota_template_association_status

        out["ServiceQuotaTemplateAssociationStatus"] = (
            capo_service_quotas.types.service_quota_template_association_status.serialize_aws_json_1_1(
                value["service_quota_template_association_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAssociationForServiceQuotaTemplateResponse:
    out: GetAssociationForServiceQuotaTemplateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceQuotaTemplateAssociationStatus" in data:
        import capo_service_quotas.types.service_quota_template_association_status

        out["service_quota_template_association_status"] = (
            capo_service_quotas.types.service_quota_template_association_status.deserialize_aws_json_1_1(
                data["ServiceQuotaTemplateAssociationStatus"]
            )
        )
    return out
