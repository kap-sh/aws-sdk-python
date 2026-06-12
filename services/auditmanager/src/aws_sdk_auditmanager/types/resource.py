"""Generated from Smithy shape ``com.amazonaws.auditmanager#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.generic_arn
    import aws_sdk_auditmanager.types.string


class Resource(TypedDict):
    arn: NotRequired["aws_sdk_auditmanager.types.generic_arn.GenericArn"]
    """<p> The Amazon Resource Name (ARN) for the resource. </p>"""
    value: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The value of the resource. </p>"""
    compliance_check: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The evaluation status for a resource that was assessed when collecting compliance check evidence. </p> <ul> <li> <p>Audit Manager classes the resource as non-compliant if Security Hub CSPM reports a <i>Fail</i> result, or if Config reports a <i>Non-compliant</i> result.</p> </li> <li> <p>Audit Manager classes the resource as compliant if Security Hub CSPM reports a <i>Pass</i> result, or if Config reports a <i>Compliant</i> result.</p> </li> <li> <p>If a compliance check isn't available or applicable, then no compliance evaluation can be made for that resource. This is the case if a resource assessment uses Config or Security Hub CSPM as the underlying data source type, but those services aren't enabled. This is also the case if the resource assessment uses an underlying data source type that doesn't support compliance checks (such as manual evidence, Amazon Web Services API calls, or CloudTrail). </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "value" in value:
        out["value"] = value["value"]
    if "compliance_check" in value:
        out["complianceCheck"] = value["compliance_check"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "value" in data:
        out["value"] = data["value"]
    if "complianceCheck" in data:
        out["compliance_check"] = data["complianceCheck"]
    return out
