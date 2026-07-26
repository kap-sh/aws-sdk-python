"""Generated from Smithy shape ``com.amazonaws.codeartifact#ResourcePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.policy_document
    import capo_codeartifact.types.policy_revision


class ResourcePolicy(TypedDict, closed=True):
    resource_arn: NotRequired["capo_codeartifact.types.arn.Arn"]
    """<p> The ARN of the resource associated with the resource policy </p>"""
    revision: NotRequired["capo_codeartifact.types.policy_revision.PolicyRevision"]
    """<p> The current revision of the resource policy. </p>"""
    document: NotRequired["capo_codeartifact.types.policy_document.PolicyDocument"]
    """<p> The resource policy formatted in JSON. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePolicy) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "document" in value:
        out["document"] = value["document"]
    return out


def deserialize_json(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "document" in data:
        out["document"] = data["document"]
    return out
