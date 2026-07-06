"""Generated from Smithy shape ``com.amazonaws.controlcatalog#AssociatedDomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.domain_arn


class AssociatedDomainSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_controlcatalog.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the related domain.</p>"""
    name: NotRequired["str"]
    """<p>The name of the related domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedDomainSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssociatedDomainSummary:
    out: AssociatedDomainSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
