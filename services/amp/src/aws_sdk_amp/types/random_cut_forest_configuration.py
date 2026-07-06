"""Generated from Smithy shape ``com.amazonaws.amp#RandomCutForestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.ignore_near_expected
    import aws_sdk_amp.types.random_cut_forest_query


class RandomCutForestConfiguration(TypedDict, closed=True):
    query: "aws_sdk_amp.types.random_cut_forest_query.RandomCutForestQuery"
    r"""<p>The Prometheus query used to retrieve the time-series data for anomaly detection.</p> <important> <p>Random Cut Forest queries must be wrapped by a supported PromQL aggregation operator. For more information, see <a href=\"https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators\">Aggregation operators</a> on the <i>Prometheus docs</i> website.</p> <p> <b>Supported PromQL aggregation operators</b>: <code>avg</code>, <code>count</code>, <code>group</code>, <code>max</code>, <code>min</code>, <code>quantile</code>, <code>stddev</code>, <code>stdvar</code>, and <code>sum</code>.</p> </important>"""
    shingle_size: "int"
    """<p>The number of consecutive data points used to create a shingle for the Random Cut Forest algorithm. The default number is 8 consecutive data points.</p>"""
    sample_size: "int"
    """<p>The number of data points sampled from the input stream for the Random Cut Forest algorithm. The default number is 256 consecutive data points.</p>"""
    ignore_near_expected_from_above: NotRequired[
        "aws_sdk_amp.types.ignore_near_expected.IgnoreNearExpected"
    ]
    """<p>Configuration for ignoring values that are near expected values from above during anomaly detection.</p>"""
    ignore_near_expected_from_below: NotRequired[
        "aws_sdk_amp.types.ignore_near_expected.IgnoreNearExpected"
    ]
    """<p>Configuration for ignoring values that are near expected values from below during anomaly detection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RandomCutForestConfiguration) -> dict:
    out: dict = {}
    out["query"] = value["query"]
    out["shingleSize"] = value.get("shingle_size", 8)
    out["sampleSize"] = value.get("sample_size", 256)
    if "ignore_near_expected_from_above" in value:
        import aws_sdk_amp.types.ignore_near_expected

        out["ignoreNearExpectedFromAbove"] = (
            aws_sdk_amp.types.ignore_near_expected.serialize_json(
                value["ignore_near_expected_from_above"]
            )
        )
    if "ignore_near_expected_from_below" in value:
        import aws_sdk_amp.types.ignore_near_expected

        out["ignoreNearExpectedFromBelow"] = (
            aws_sdk_amp.types.ignore_near_expected.serialize_json(
                value["ignore_near_expected_from_below"]
            )
        )
    return out


def deserialize_json(data: dict) -> RandomCutForestConfiguration:
    out: RandomCutForestConfiguration = {}  # type: ignore[typeddict-item]
    if "query" in data:
        out["query"] = data["query"]
    else:
        raise DeserializationError("RandomCutForestConfiguration.query required")
    if "shingleSize" in data:
        out["shingle_size"] = data["shingleSize"]
    else:
        out["shingle_size"] = 8
    if "sampleSize" in data:
        out["sample_size"] = data["sampleSize"]
    else:
        out["sample_size"] = 256
    if "ignoreNearExpectedFromAbove" in data:
        import aws_sdk_amp.types.ignore_near_expected

        out["ignore_near_expected_from_above"] = (
            aws_sdk_amp.types.ignore_near_expected.deserialize_json(
                data["ignoreNearExpectedFromAbove"]
            )
        )
    if "ignoreNearExpectedFromBelow" in data:
        import aws_sdk_amp.types.ignore_near_expected

        out["ignore_near_expected_from_below"] = (
            aws_sdk_amp.types.ignore_near_expected.deserialize_json(
                data["ignoreNearExpectedFromBelow"]
            )
        )
    return out
