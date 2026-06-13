"""Generated from Smithy shape ``com.amazonaws.amp#LimitsPerLabelSet``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.label_set
    import aws_sdk_amp.types.limits_per_label_set_entry


class LimitsPerLabelSet(TypedDict):
    limits: "aws_sdk_amp.types.limits_per_label_set_entry.LimitsPerLabelSetEntry"
    """<p>This structure contains the information about the limits that apply to time series that match this label set.</p>"""
    label_set: "aws_sdk_amp.types.label_set.LabelSet"
    """<p>This defines one label set that will have an enforced active time series limit. </p> <p>Label values accept ASCII characters and must contain at least one character that isn't whitespace. ASCII control characters are not accepted. If the label name is metric name label <code>__<i>name</i>__</code>, then the <i>metric</i> part of the name must conform to the following pattern: <code>[a-zA-Z_:][a-zA-Z0-9_:]*</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitsPerLabelSet) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.limits_per_label_set_entry

    out["limits"] = aws_sdk_amp.types.limits_per_label_set_entry.serialize_json(
        value["limits"]
    )
    import aws_sdk_amp.types.label_set

    out["labelSet"] = aws_sdk_amp.types.label_set.serialize_json(value["label_set"])
    return out


def deserialize_json(data: dict) -> LimitsPerLabelSet:
    out: LimitsPerLabelSet = {}  # type: ignore[typeddict-item]
    if "limits" in data:
        import aws_sdk_amp.types.limits_per_label_set_entry

        out["limits"] = aws_sdk_amp.types.limits_per_label_set_entry.deserialize_json(
            data["limits"]
        )
    else:
        raise DeserializationError("LimitsPerLabelSet.limits required")
    if "labelSet" in data:
        import aws_sdk_amp.types.label_set

        out["label_set"] = aws_sdk_amp.types.label_set.deserialize_json(
            data["labelSet"]
        )
    else:
        raise DeserializationError("LimitsPerLabelSet.label_set required")
    return out
