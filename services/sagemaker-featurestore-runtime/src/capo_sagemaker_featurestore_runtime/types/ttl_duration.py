"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#TtlDuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.ttl_duration_unit
    import capo_sagemaker_featurestore_runtime.types.ttl_duration_value


class TtlDuration(TypedDict, closed=True):
    unit: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.ttl_duration_unit.TtlDurationUnit"
    ]
    """<p> <code>TtlDuration</code> time unit.</p>"""
    value: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.ttl_duration_value.TtlDurationValue"
    ]
    """<p> <code>TtlDuration</code> time value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TtlDuration) -> dict:
    out: dict = {}
    if "unit" in value:
        import capo_sagemaker_featurestore_runtime.types.ttl_duration_unit

        out["Unit"] = (
            capo_sagemaker_featurestore_runtime.types.ttl_duration_unit.serialize_json(
                value["unit"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TtlDuration:
    out: TtlDuration = {}  # type: ignore[typeddict-item]
    if "Unit" in data:
        import capo_sagemaker_featurestore_runtime.types.ttl_duration_unit

        out["unit"] = (
            capo_sagemaker_featurestore_runtime.types.ttl_duration_unit.deserialize_json(
                data["Unit"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
