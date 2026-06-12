"""Generated from Smithy shape ``com.amazonaws.costexplorer#RootCauseImpact``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_double


class RootCauseImpact(TypedDict):
    contribution: "aws_sdk_cost_explorer.types.generic_double.GenericDouble"
    """<p>The dollar amount that this root cause contributed to the anomaly's TotalImpact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RootCauseImpact) -> dict:
    out: dict = {}
    out["Contribution"] = value.get("contribution", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RootCauseImpact:
    out: RootCauseImpact = {}  # type: ignore[typeddict-item]
    if "Contribution" in data:
        out["contribution"] = data["Contribution"]
    else:
        out["contribution"] = 0
    return out
