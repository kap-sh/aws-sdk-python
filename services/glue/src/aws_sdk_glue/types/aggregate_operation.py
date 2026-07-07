"""Generated from Smithy shape ``com.amazonaws.glue#AggregateOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.agg_function
    import aws_sdk_glue.types.enclosed_in_string_properties


class AggregateOperation(TypedDict, closed=True):
    column: (
        "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    )
    """<p>Specifies the column on the data set on which the aggregation function will be applied.</p>"""
    agg_func: "aws_sdk_glue.types.agg_function.AggFunction"
    """<p>Specifies the aggregation function to apply.</p> <p>Possible aggregation functions include: avg countDistinct, count, first, last, kurtosis, max, min, skewness, stddev_samp, stddev_pop, sum, sumDistinct, var_samp, var_pop</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateOperation) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["Column"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["column"]
        )
    )
    import aws_sdk_glue.types.agg_function

    out["AggFunc"] = aws_sdk_glue.types.agg_function.serialize_aws_json_1_1(
        value["agg_func"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateOperation:
    out: AggregateOperation = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["column"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Column"]
            )
        )
    else:
        raise DeserializationError("AggregateOperation.column required")
    if "AggFunc" in data:
        import aws_sdk_glue.types.agg_function

        out["agg_func"] = aws_sdk_glue.types.agg_function.deserialize_aws_json_1_1(
            data["AggFunc"]
        )
    else:
        raise DeserializationError("AggregateOperation.agg_func required")
    return out
