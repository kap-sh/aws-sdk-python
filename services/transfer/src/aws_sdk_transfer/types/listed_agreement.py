"""Generated from Smithy shape ``com.amazonaws.transfer#ListedAgreement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.agreement_id
    import aws_sdk_transfer.types.agreement_status_type
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.description
    import aws_sdk_transfer.types.profile_id
    import aws_sdk_transfer.types.server_id


class ListedAgreement(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_transfer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the specified agreement.</p>"""
    agreement_id: NotRequired["aws_sdk_transfer.types.agreement_id.AgreementId"]
    """<p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>"""
    description: NotRequired["aws_sdk_transfer.types.description.Description"]
    """<p>The current description for the agreement. You can change it by calling the <code>UpdateAgreement</code> operation and providing a new description. </p>"""
    status: NotRequired[
        "aws_sdk_transfer.types.agreement_status_type.AgreementStatusType"
    ]
    """<p>The agreement can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    server_id: NotRequired["aws_sdk_transfer.types.server_id.ServerId"]
    """<p>The unique identifier for the agreement.</p>"""
    local_profile_id: NotRequired["aws_sdk_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the AS2 local profile.</p>"""
    partner_profile_id: NotRequired["aws_sdk_transfer.types.profile_id.ProfileId"]
    """<p>A unique identifier for the partner profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedAgreement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "agreement_id" in value:
        out["AgreementId"] = value["agreement_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_transfer.types.agreement_status_type

        out["Status"] = (
            aws_sdk_transfer.types.agreement_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "server_id" in value:
        out["ServerId"] = value["server_id"]
    if "local_profile_id" in value:
        out["LocalProfileId"] = value["local_profile_id"]
    if "partner_profile_id" in value:
        out["PartnerProfileId"] = value["partner_profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedAgreement:
    out: ListedAgreement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AgreementId" in data:
        out["agreement_id"] = data["AgreementId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_transfer.types.agreement_status_type

        out["status"] = (
            aws_sdk_transfer.types.agreement_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    if "LocalProfileId" in data:
        out["local_profile_id"] = data["LocalProfileId"]
    if "PartnerProfileId" in data:
        out["partner_profile_id"] = data["PartnerProfileId"]
    return out
