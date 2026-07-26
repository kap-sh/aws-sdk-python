"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AssociateBenefitApplicationResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_application_id


class AssociateBenefitApplicationResourceOutput(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_benefits.types.benefit_application_id.BenefitApplicationId"
    ]
    """<p>The unique identifier of the benefit application after the resource association.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the benefit application after the resource association.</p>"""
    revision: NotRequired["str"]
    """<p>The updated revision number of the benefit application after the resource association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateBenefitApplicationResourceOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateBenefitApplicationResourceOutput:
    out: AssociateBenefitApplicationResourceOutput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Revision" in data:
        out["revision"] = data["Revision"]
    return out
