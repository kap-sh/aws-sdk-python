"""Generated from Smithy shape ``com.amazonaws.aiops#CreateInvestigationGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_arn


class CreateInvestigationGroupOutput(TypedDict):
    arn: NotRequired[
        "aws_sdk_aiops.types.investigation_group_arn.InvestigationGroupArn"
    ]
    """<p>The ARN of the investigation group that you just created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInvestigationGroupOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateInvestigationGroupOutput:
    out: CreateInvestigationGroupOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
