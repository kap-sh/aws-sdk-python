"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleDimension``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_dimension_key
    import aws_sdk_compute_optimizer.types.idle_dimension_values


class IdleDimension(TypedDict):
    key: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_dimension_key.IdleDimensionKey"
    ]
    """<p>The name of the dimension key.</p>"""
    values: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_dimension_values.IdleDimensionValues"
    ]
    """<p>The value of the dimension.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleDimension) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "values" in value:
        import aws_sdk_compute_optimizer.types.idle_dimension_values

        out["values"] = (
            aws_sdk_compute_optimizer.types.idle_dimension_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleDimension:
    out: IdleDimension = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "values" in data:
        import aws_sdk_compute_optimizer.types.idle_dimension_values

        out["values"] = (
            aws_sdk_compute_optimizer.types.idle_dimension_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
