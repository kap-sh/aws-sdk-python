"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptPredictionsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.accept_choices
    import aws_sdk_datazone.types.accept_rule
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.revision

class AcceptPredictionsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the asset.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision that is to be made to the asset.</p>"""
    accept_rule: NotRequired["aws_sdk_datazone.types.accept_rule.AcceptRule"]
    """<p>Specifies the rule (or the conditions) under which a prediction can be accepted.</p>"""
    accept_choices: NotRequired["aws_sdk_datazone.types.accept_choices.AcceptChoices"]
    """<p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be accepted.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AcceptPredictionsInput) -> dict:
    out: dict = {}
    if "accept_rule" in value:
        import aws_sdk_datazone.types.accept_rule
        out["acceptRule"] = aws_sdk_datazone.types.accept_rule.serialize_json(value["accept_rule"])
    if "accept_choices" in value:
        import aws_sdk_datazone.types.accept_choices
        out["acceptChoices"] = aws_sdk_datazone.types.accept_choices.serialize_json(value["accept_choices"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AcceptPredictionsInput:
    out: AcceptPredictionsInput = {}  # type: ignore[typeddict-item]
    if "acceptRule" in data:
        import aws_sdk_datazone.types.accept_rule
        out["accept_rule"] = aws_sdk_datazone.types.accept_rule.deserialize_json(data["acceptRule"])
    if "acceptChoices" in data:
        import aws_sdk_datazone.types.accept_choices
        out["accept_choices"] = aws_sdk_datazone.types.accept_choices.deserialize_json(data["acceptChoices"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out