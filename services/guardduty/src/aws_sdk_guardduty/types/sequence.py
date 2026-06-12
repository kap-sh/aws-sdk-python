"""Generated from Smithy shape ``com.amazonaws.guardduty#Sequence``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.actors
    import aws_sdk_guardduty.types.additional_sequence_types
    import aws_sdk_guardduty.types.indicators
    import aws_sdk_guardduty.types.network_endpoints
    import aws_sdk_guardduty.types.resources
    import aws_sdk_guardduty.types.sequence_description
    import aws_sdk_guardduty.types.signals
    import aws_sdk_guardduty.types.string


class Sequence(TypedDict):
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Unique identifier of the attack sequence.</p>"""
    description: NotRequired[
        "aws_sdk_guardduty.types.sequence_description.SequenceDescription"
    ]
    """<p>Description of the attack sequence.</p>"""
    actors: NotRequired["aws_sdk_guardduty.types.actors.Actors"]
    """<p>Contains information about the actors involved in the attack sequence.</p>"""
    resources: NotRequired["aws_sdk_guardduty.types.resources.Resources"]
    """<p>Contains information about the resources involved in the attack sequence.</p>"""
    endpoints: NotRequired["aws_sdk_guardduty.types.network_endpoints.NetworkEndpoints"]
    """<p>Contains information about the network endpoints that were used in the attack sequence.</p>"""
    signals: NotRequired["aws_sdk_guardduty.types.signals.Signals"]
    """<p>Contains information about the signals involved in the attack sequence.</p>"""
    sequence_indicators: NotRequired["aws_sdk_guardduty.types.indicators.Indicators"]
    """<p>Contains information about the indicators observed in the attack sequence.</p>"""
    additional_sequence_types: NotRequired[
        "aws_sdk_guardduty.types.additional_sequence_types.AdditionalSequenceTypes"
    ]
    """<p>Additional types of sequences that may be associated with the attack sequence finding, providing further context about the nature of the detected threat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sequence) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "description" in value:
        out["description"] = value["description"]
    if "actors" in value:
        import aws_sdk_guardduty.types.actors

        out["actors"] = aws_sdk_guardduty.types.actors.serialize_json(value["actors"])
    if "resources" in value:
        import aws_sdk_guardduty.types.resources

        out["resources"] = aws_sdk_guardduty.types.resources.serialize_json(
            value["resources"]
        )
    if "endpoints" in value:
        import aws_sdk_guardduty.types.network_endpoints

        out["endpoints"] = aws_sdk_guardduty.types.network_endpoints.serialize_json(
            value["endpoints"]
        )
    if "signals" in value:
        import aws_sdk_guardduty.types.signals

        out["signals"] = aws_sdk_guardduty.types.signals.serialize_json(
            value["signals"]
        )
    if "sequence_indicators" in value:
        import aws_sdk_guardduty.types.indicators

        out["sequenceIndicators"] = aws_sdk_guardduty.types.indicators.serialize_json(
            value["sequence_indicators"]
        )
    if "additional_sequence_types" in value:
        import aws_sdk_guardduty.types.additional_sequence_types

        out["additionalSequenceTypes"] = (
            aws_sdk_guardduty.types.additional_sequence_types.serialize_json(
                value["additional_sequence_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> Sequence:
    out: Sequence = {}  # type: ignore[typeddict-item]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "description" in data:
        out["description"] = data["description"]
    if "actors" in data:
        import aws_sdk_guardduty.types.actors

        out["actors"] = aws_sdk_guardduty.types.actors.deserialize_json(data["actors"])
    if "resources" in data:
        import aws_sdk_guardduty.types.resources

        out["resources"] = aws_sdk_guardduty.types.resources.deserialize_json(
            data["resources"]
        )
    if "endpoints" in data:
        import aws_sdk_guardduty.types.network_endpoints

        out["endpoints"] = aws_sdk_guardduty.types.network_endpoints.deserialize_json(
            data["endpoints"]
        )
    if "signals" in data:
        import aws_sdk_guardduty.types.signals

        out["signals"] = aws_sdk_guardduty.types.signals.deserialize_json(
            data["signals"]
        )
    if "sequenceIndicators" in data:
        import aws_sdk_guardduty.types.indicators

        out["sequence_indicators"] = (
            aws_sdk_guardduty.types.indicators.deserialize_json(
                data["sequenceIndicators"]
            )
        )
    if "additionalSequenceTypes" in data:
        import aws_sdk_guardduty.types.additional_sequence_types

        out["additional_sequence_types"] = (
            aws_sdk_guardduty.types.additional_sequence_types.deserialize_json(
                data["additionalSequenceTypes"]
            )
        )
    return out
