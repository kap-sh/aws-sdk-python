"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptSubscriptionRequestInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.accepted_asset_scopes
    import aws_sdk_datazone.types.asset_permissions
    import aws_sdk_datazone.types.decision_comment
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_request_id

class AcceptSubscriptionRequestInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The Amazon DataZone domain where the specified subscription request is being accepted.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The unique identifier of the subscription request that is to be accepted.</p>"""
    decision_comment: NotRequired["aws_sdk_datazone.types.decision_comment.DecisionComment"]
    """<p>A description that specifies the reason for accepting the specified subscription request.</p>"""
    asset_scopes: NotRequired["aws_sdk_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"]
    """<p>The asset scopes of the accept subscription request.</p>"""
    asset_permissions: NotRequired["aws_sdk_datazone.types.asset_permissions.AssetPermissions"]
    """<p>The asset permissions of the accept subscription request.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AcceptSubscriptionRequestInput) -> dict:
    out: dict = {}
    if "decision_comment" in value:
        out["decisionComment"] = value["decision_comment"]
    if "asset_scopes" in value:
        import aws_sdk_datazone.types.accepted_asset_scopes
        out["assetScopes"] = aws_sdk_datazone.types.accepted_asset_scopes.serialize_json(value["asset_scopes"])
    if "asset_permissions" in value:
        import aws_sdk_datazone.types.asset_permissions
        out["assetPermissions"] = aws_sdk_datazone.types.asset_permissions.serialize_json(value["asset_permissions"])
    return out


def deserialize_json(data: dict) -> AcceptSubscriptionRequestInput:
    out: AcceptSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    if "decisionComment" in data:
        out["decision_comment"] = data["decisionComment"]
    if "assetScopes" in data:
        import aws_sdk_datazone.types.accepted_asset_scopes
        out["asset_scopes"] = aws_sdk_datazone.types.accepted_asset_scopes.deserialize_json(data["assetScopes"])
    if "assetPermissions" in data:
        import aws_sdk_datazone.types.asset_permissions
        out["asset_permissions"] = aws_sdk_datazone.types.asset_permissions.deserialize_json(data["assetPermissions"])
    return out