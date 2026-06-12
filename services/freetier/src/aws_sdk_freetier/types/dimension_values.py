"""Generated from Smithy shape ``com.amazonaws.freetier#DimensionValues``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_freetier.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_freetier.types.dimension
    import aws_sdk_freetier.types.match_options
    import aws_sdk_freetier.types.values

class DimensionValues(TypedDict):
    key: "aws_sdk_freetier.types.dimension.Dimension"
    """<p>The name of the dimension that you want to filter on.</p>"""
    values: "aws_sdk_freetier.types.values.Values"
    """<p>The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.</p>"""
    match_options: "aws_sdk_freetier.types.match_options.MatchOptions"
    """<p>The match options that you can use to filter your results. You can specify only one of these values in the array.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionValues) -> dict:
    out: dict = {}
    import aws_sdk_freetier.types.dimension
    out["Key"] = aws_sdk_freetier.types.dimension.serialize_aws_json_1_0(value["key"])
    import aws_sdk_freetier.types.values
    out["Values"] = aws_sdk_freetier.types.values.serialize_aws_json_1_0(value["values"])
    import aws_sdk_freetier.types.match_options
    out["MatchOptions"] = aws_sdk_freetier.types.match_options.serialize_aws_json_1_0(value["match_options"])
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionValues:
    out: DimensionValues = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_freetier.types.dimension
        out["key"] = aws_sdk_freetier.types.dimension.deserialize_aws_json_1_0(data["Key"])
    else:
        raise DeserializationError("DimensionValues.key required")
    if "Values" in data:
        import aws_sdk_freetier.types.values
        out["values"] = aws_sdk_freetier.types.values.deserialize_aws_json_1_0(data["Values"])
    else:
        raise DeserializationError("DimensionValues.values required")
    if "MatchOptions" in data:
        import aws_sdk_freetier.types.match_options
        out["match_options"] = aws_sdk_freetier.types.match_options.deserialize_aws_json_1_0(data["MatchOptions"])
    else:
        raise DeserializationError("DimensionValues.match_options required")
    return out