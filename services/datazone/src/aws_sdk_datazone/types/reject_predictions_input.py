"""Generated from Smithy shape ``com.amazonaws.datazone#RejectPredictionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.reject_choices
    import aws_sdk_datazone.types.reject_rule
    import aws_sdk_datazone.types.revision


class RejectPredictionsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the prediction.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision that is to be made to the asset.</p>"""
    reject_rule: NotRequired["aws_sdk_datazone.types.reject_rule.RejectRule"]
    """<p>Specifies the rule (or the conditions) under which a prediction can be rejected.</p>"""
    reject_choices: NotRequired["aws_sdk_datazone.types.reject_choices.RejectChoices"]
    """<p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be rejected.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectPredictionsInput) -> dict:
    out: dict = {}
    if "reject_rule" in value:
        import aws_sdk_datazone.types.reject_rule

        out["rejectRule"] = aws_sdk_datazone.types.reject_rule.serialize_json(
            value["reject_rule"]
        )
    if "reject_choices" in value:
        import aws_sdk_datazone.types.reject_choices

        out["rejectChoices"] = aws_sdk_datazone.types.reject_choices.serialize_json(
            value["reject_choices"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RejectPredictionsInput:
    out: RejectPredictionsInput = {}  # type: ignore[typeddict-item]
    if "rejectRule" in data:
        import aws_sdk_datazone.types.reject_rule

        out["reject_rule"] = aws_sdk_datazone.types.reject_rule.deserialize_json(
            data["rejectRule"]
        )
    if "rejectChoices" in data:
        import aws_sdk_datazone.types.reject_choices

        out["reject_choices"] = aws_sdk_datazone.types.reject_choices.deserialize_json(
            data["rejectChoices"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
