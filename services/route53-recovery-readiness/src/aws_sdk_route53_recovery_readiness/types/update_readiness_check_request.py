"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#UpdateReadinessCheckRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class UpdateReadinessCheckRequest(TypedDict):
    readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a readiness check.</p>"""
    resource_set_name: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The name of the resource set to be checked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReadinessCheckRequest) -> dict:
    out: dict = {}
    if "resource_set_name" in value:
        out["resourceSetName"] = value["resource_set_name"]
    return out


def deserialize_json(data: dict) -> UpdateReadinessCheckRequest:
    out: UpdateReadinessCheckRequest = {}  # type: ignore[typeddict-item]
    if "resourceSetName" in data:
        out["resource_set_name"] = data["resourceSetName"]
    return out
