"""Generated from Smithy shape ``com.amazonaws.datazone#RejectPredictionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_identifier
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.reject_choices
    import capo_datazone.types.reject_rule
    import capo_datazone.types.revision


class RejectPredictionsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    identifier: "capo_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the prediction.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision that is to be made to the asset.</p>"""
    reject_rule: NotRequired["capo_datazone.types.reject_rule.RejectRule"]
    """<p>Specifies the rule (or the conditions) under which a prediction can be rejected.</p>"""
    reject_choices: NotRequired["capo_datazone.types.reject_choices.RejectChoices"]
    """<p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be rejected.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectPredictionsInput) -> dict:
    out: dict = {}
    if "reject_rule" in value:
        import capo_datazone.types.reject_rule

        out["rejectRule"] = capo_datazone.types.reject_rule.serialize_json(
            value["reject_rule"]
        )
    if "reject_choices" in value:
        import capo_datazone.types.reject_choices

        out["rejectChoices"] = capo_datazone.types.reject_choices.serialize_json(
            value["reject_choices"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RejectPredictionsInput:
    out: RejectPredictionsInput = {}  # type: ignore[typeddict-item]
    if "rejectRule" in data:
        import capo_datazone.types.reject_rule

        out["reject_rule"] = capo_datazone.types.reject_rule.deserialize_json(
            data["rejectRule"]
        )
    if "rejectChoices" in data:
        import capo_datazone.types.reject_choices

        out["reject_choices"] = capo_datazone.types.reject_choices.deserialize_json(
            data["rejectChoices"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
