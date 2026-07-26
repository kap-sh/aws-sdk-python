"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class StandardsControlAssociationId(TypedDict, closed=True):
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The unique identifier (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) of a security control across standards. </p>"""
    standards_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of a standard. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationId) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    return out


def deserialize_json(data: dict) -> StandardsControlAssociationId:
    out: StandardsControlAssociationId = {}  # type: ignore[typeddict-item]
    if "SecurityControlId" in data:
        out["security_control_id"] = data["SecurityControlId"]
    if "StandardsArn" in data:
        out["standards_arn"] = data["StandardsArn"]
    return out
