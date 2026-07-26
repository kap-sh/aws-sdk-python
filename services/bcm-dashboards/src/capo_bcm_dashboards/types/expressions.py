"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Expressions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.expression

Expressions: TypeAlias = list["capo_bcm_dashboards.types.expression.Expression"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expressions) -> list:
    import capo_bcm_dashboards.types.expression

    out: list = []
    for item in value:
        out.append(capo_bcm_dashboards.types.expression.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Expressions:
    import capo_bcm_dashboards.types.expression

    out: Expressions = []
    for item in data:
        out.append(capo_bcm_dashboards.types.expression.deserialize_aws_json_1_0(item))
    return out
