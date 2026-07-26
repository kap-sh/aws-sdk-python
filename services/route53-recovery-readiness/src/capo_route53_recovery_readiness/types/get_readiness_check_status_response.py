"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetReadinessCheckStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_message
    import capo_route53_recovery_readiness.types.__list_of_resource_result
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.readiness


class GetReadinessCheckStatusResponse(TypedDict, closed=True):
    messages: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_message.__listOfMessage"
    ]
    """<p>Top level messages for readiness check status</p>"""
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness: NotRequired["capo_route53_recovery_readiness.types.readiness.Readiness"]
    """<p>The readiness at rule level.</p>"""
    resources: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_resource_result.__listOfResourceResult"
    ]
    """<p>Summary of the readiness of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadinessCheckStatusResponse) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_route53_recovery_readiness.types.__list_of_message

        out["messages"] = (
            capo_route53_recovery_readiness.types.__list_of_message.serialize_json(
                value["messages"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "readiness" in value:
        import capo_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            capo_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "resources" in value:
        import capo_route53_recovery_readiness.types.__list_of_resource_result

        out["resources"] = (
            capo_route53_recovery_readiness.types.__list_of_resource_result.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetReadinessCheckStatusResponse:
    out: GetReadinessCheckStatusResponse = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import capo_route53_recovery_readiness.types.__list_of_message

        out["messages"] = (
            capo_route53_recovery_readiness.types.__list_of_message.deserialize_json(
                data["messages"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "readiness" in data:
        import capo_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            capo_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "resources" in data:
        import capo_route53_recovery_readiness.types.__list_of_resource_result

        out["resources"] = (
            capo_route53_recovery_readiness.types.__list_of_resource_result.deserialize_json(
                data["resources"]
            )
        )
    return out
