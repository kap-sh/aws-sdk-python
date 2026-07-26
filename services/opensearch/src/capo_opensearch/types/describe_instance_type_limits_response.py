"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInstanceTypeLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.limits_by_role


class DescribeInstanceTypeLimitsResponse(TypedDict, closed=True):
    limits_by_role: NotRequired["capo_opensearch.types.limits_by_role.LimitsByRole"]
    """<p>Map that contains all applicable instance type limits.<code>data</code> refers to data nodes.<code>master</code> refers to dedicated master nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceTypeLimitsResponse) -> dict:
    out: dict = {}
    if "limits_by_role" in value:
        import capo_opensearch.types.limits_by_role

        out["LimitsByRole"] = capo_opensearch.types.limits_by_role.serialize_json(
            value["limits_by_role"]
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceTypeLimitsResponse:
    out: DescribeInstanceTypeLimitsResponse = {}  # type: ignore[typeddict-item]
    if "LimitsByRole" in data:
        import capo_opensearch.types.limits_by_role

        out["limits_by_role"] = capo_opensearch.types.limits_by_role.deserialize_json(
            data["LimitsByRole"]
        )
    return out
