"""Generated from Smithy shape ``com.amazonaws.guardduty#Indicator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.indicator_title
    import aws_sdk_guardduty.types.indicator_type
    import aws_sdk_guardduty.types.indicator_values


class Indicator(TypedDict):
    key: NotRequired["aws_sdk_guardduty.types.indicator_type.IndicatorType"]
    """<p>Specific indicator keys observed in the attack sequence. For description of the valid values for key, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-summary.html#guardduty-extended-threat-detection-attack-sequence-finding-details\">Attack sequence finding details</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    values: NotRequired["aws_sdk_guardduty.types.indicator_values.IndicatorValues"]
    """<p>Values associated with each indicator key. For example, if the indicator key is <code>SUSPICIOUS_NETWORK</code>, then the value will be the name of the network. If the indicator key is <code>ATTACK_TACTIC</code>, then the value will be one of the MITRE tactics. </p>"""
    title: NotRequired["aws_sdk_guardduty.types.indicator_title.IndicatorTitle"]
    """<p>Title describing the indicator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Indicator) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_guardduty.types.indicator_type

        out["key"] = aws_sdk_guardduty.types.indicator_type.serialize_json(value["key"])
    if "values" in value:
        import aws_sdk_guardduty.types.indicator_values

        out["values"] = aws_sdk_guardduty.types.indicator_values.serialize_json(
            value["values"]
        )
    if "title" in value:
        out["title"] = value["title"]
    return out


def deserialize_json(data: dict) -> Indicator:
    out: Indicator = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_guardduty.types.indicator_type

        out["key"] = aws_sdk_guardduty.types.indicator_type.deserialize_json(
            data["key"]
        )
    if "values" in data:
        import aws_sdk_guardduty.types.indicator_values

        out["values"] = aws_sdk_guardduty.types.indicator_values.deserialize_json(
            data["values"]
        )
    if "title" in data:
        out["title"] = data["title"]
    return out
