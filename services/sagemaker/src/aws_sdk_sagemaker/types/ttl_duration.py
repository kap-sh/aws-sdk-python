"""Generated from Smithy shape ``com.amazonaws.sagemaker#TtlDuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ttl_duration_unit
    import aws_sdk_sagemaker.types.ttl_duration_value


class TtlDuration(TypedDict):
    unit: NotRequired["aws_sdk_sagemaker.types.ttl_duration_unit.TtlDurationUnit"]
    """<p> <code>TtlDuration</code> time unit.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.ttl_duration_value.TtlDurationValue"]
    """<p> <code>TtlDuration</code> time value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TtlDuration) -> dict:
    out: dict = {}
    if "unit" in value:
        import aws_sdk_sagemaker.types.ttl_duration_unit

        out["Unit"] = aws_sdk_sagemaker.types.ttl_duration_unit.serialize_aws_json_1_1(
            value["unit"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TtlDuration:
    out: TtlDuration = {}  # type: ignore[typeddict-item]
    if "Unit" in data:
        import aws_sdk_sagemaker.types.ttl_duration_unit

        out["unit"] = (
            aws_sdk_sagemaker.types.ttl_duration_unit.deserialize_aws_json_1_1(
                data["Unit"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
