"""Generated from Smithy shape ``com.amazonaws.securityhub#Sequence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.actors_list
    import aws_sdk_securityhub.types.indicators_list
    import aws_sdk_securityhub.types.network_endpoints_list
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.signals_list


class Sequence(TypedDict, closed=True):
    uid: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Unique identifier of the attack sequence. </p>"""
    actors: NotRequired["aws_sdk_securityhub.types.actors_list.ActorsList"]
    """<p> Provides information about the actors involved in the attack sequence. </p>"""
    endpoints: NotRequired[
        "aws_sdk_securityhub.types.network_endpoints_list.NetworkEndpointsList"
    ]
    """<p> Contains information about the network endpoints that were used in the attack sequence. </p>"""
    signals: NotRequired["aws_sdk_securityhub.types.signals_list.SignalsList"]
    """<p> Contains information about the signals involved in the attack sequence. </p>"""
    sequence_indicators: NotRequired[
        "aws_sdk_securityhub.types.indicators_list.IndicatorsList"
    ]
    r"""<p> Contains information about the indicators observed in the attack sequence. The values for <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Signal.html\">SignalIndicators</a> are a subset of the values for <code>SequenceIndicators</code>, but the values for these fields don't always match 1:1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sequence) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "actors" in value:
        import aws_sdk_securityhub.types.actors_list

        out["Actors"] = aws_sdk_securityhub.types.actors_list.serialize_json(
            value["actors"]
        )
    if "endpoints" in value:
        import aws_sdk_securityhub.types.network_endpoints_list

        out["Endpoints"] = (
            aws_sdk_securityhub.types.network_endpoints_list.serialize_json(
                value["endpoints"]
            )
        )
    if "signals" in value:
        import aws_sdk_securityhub.types.signals_list

        out["Signals"] = aws_sdk_securityhub.types.signals_list.serialize_json(
            value["signals"]
        )
    if "sequence_indicators" in value:
        import aws_sdk_securityhub.types.indicators_list

        out["SequenceIndicators"] = (
            aws_sdk_securityhub.types.indicators_list.serialize_json(
                value["sequence_indicators"]
            )
        )
    return out


def deserialize_json(data: dict) -> Sequence:
    out: Sequence = {}  # type: ignore[typeddict-item]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    if "Actors" in data:
        import aws_sdk_securityhub.types.actors_list

        out["actors"] = aws_sdk_securityhub.types.actors_list.deserialize_json(
            data["Actors"]
        )
    if "Endpoints" in data:
        import aws_sdk_securityhub.types.network_endpoints_list

        out["endpoints"] = (
            aws_sdk_securityhub.types.network_endpoints_list.deserialize_json(
                data["Endpoints"]
            )
        )
    if "Signals" in data:
        import aws_sdk_securityhub.types.signals_list

        out["signals"] = aws_sdk_securityhub.types.signals_list.deserialize_json(
            data["Signals"]
        )
    if "SequenceIndicators" in data:
        import aws_sdk_securityhub.types.indicators_list

        out["sequence_indicators"] = (
            aws_sdk_securityhub.types.indicators_list.deserialize_json(
                data["SequenceIndicators"]
            )
        )
    return out
