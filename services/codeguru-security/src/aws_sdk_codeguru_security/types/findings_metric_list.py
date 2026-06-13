"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingsMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.account_findings_metric

FindingsMetricList: TypeAlias = list[
    "aws_sdk_codeguru_security.types.account_findings_metric.AccountFindingsMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsMetricList) -> list:
    import aws_sdk_codeguru_security.types.account_findings_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_security.types.account_findings_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsMetricList:
    import aws_sdk_codeguru_security.types.account_findings_metric

    out: FindingsMetricList = []
    for item in data:
        out.append(
            aws_sdk_codeguru_security.types.account_findings_metric.deserialize_json(
                item
            )
        )
    return out
