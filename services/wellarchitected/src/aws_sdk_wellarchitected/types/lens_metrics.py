"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_metric

LensMetrics: TypeAlias = list["aws_sdk_wellarchitected.types.lens_metric.LensMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: LensMetrics) -> list:
    import aws_sdk_wellarchitected.types.lens_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.lens_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> LensMetrics:
    import aws_sdk_wellarchitected.types.lens_metric

    out: LensMetrics = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.lens_metric.deserialize_json(item))
    return out
