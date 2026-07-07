"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_double
    import aws_sdk_xray.types.sampling_strategy_name


class SamplingStrategy(TypedDict, closed=True):
    name: NotRequired["aws_sdk_xray.types.sampling_strategy_name.SamplingStrategyName"]
    """<p>The name of a sampling rule.</p>"""
    value: NotRequired["aws_sdk_xray.types.nullable_double.NullableDouble"]
    """<p>The value of a sampling rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStrategy) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_xray.types.sampling_strategy_name

        out["Name"] = aws_sdk_xray.types.sampling_strategy_name.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SamplingStrategy:
    out: SamplingStrategy = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_xray.types.sampling_strategy_name

        out["name"] = aws_sdk_xray.types.sampling_strategy_name.deserialize_json(
            data["Name"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
