"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#CreateReadinessCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.tags


class CreateReadinessCheckRequest(TypedDict, closed=True):
    readiness_check_name: NotRequired[
        "capo_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The name of the readiness check to create.</p>"""
    resource_set_name: NotRequired[
        "capo_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The name of the resource set to check.</p>"""
    tags: NotRequired["capo_route53_recovery_readiness.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateReadinessCheckRequest) -> dict:
    out: dict = {}
    if "readiness_check_name" in value:
        out["readinessCheckName"] = value["readiness_check_name"]
    if "resource_set_name" in value:
        out["resourceSetName"] = value["resource_set_name"]
    if "tags" in value:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateReadinessCheckRequest:
    out: CreateReadinessCheckRequest = {}  # type: ignore[typeddict-item]
    if "readinessCheckName" in data:
        out["readiness_check_name"] = data["readinessCheckName"]
    if "resourceSetName" in data:
        out["resource_set_name"] = data["resourceSetName"]
    if "tags" in data:
        import capo_route53_recovery_readiness.types.tags

        out["tags"] = capo_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
