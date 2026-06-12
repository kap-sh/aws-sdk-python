"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#DisassociateBenefitApplicationResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_id


class DisassociateBenefitApplicationResourceOutput(TypedDict):
    id: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_id.BenefitApplicationId"
    ]
    """<p>The unique identifier of the benefit application after the resource disassociation.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the benefit application after the resource disassociation.</p>"""
    revision: NotRequired["str"]
    """<p>The updated revision number of the benefit application after the resource disassociation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateBenefitApplicationResourceOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DisassociateBenefitApplicationResourceOutput:
    out: DisassociateBenefitApplicationResourceOutput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Revision" in data:
        out["revision"] = data["Revision"]
    return out
