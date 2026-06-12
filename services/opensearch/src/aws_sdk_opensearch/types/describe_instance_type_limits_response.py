"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInstanceTypeLimitsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.limits_by_role


class DescribeInstanceTypeLimitsResponse(TypedDict):
    limits_by_role: NotRequired["aws_sdk_opensearch.types.limits_by_role.LimitsByRole"]
    """<p>Map that contains all applicable instance type limits.<code>data</code> refers to data nodes.<code>master</code> refers to dedicated master nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceTypeLimitsResponse) -> dict:
    out: dict = {}
    if "limits_by_role" in value:
        import aws_sdk_opensearch.types.limits_by_role

        out["LimitsByRole"] = aws_sdk_opensearch.types.limits_by_role.serialize_json(
            value["limits_by_role"]
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceTypeLimitsResponse:
    out: DescribeInstanceTypeLimitsResponse = {}  # type: ignore[typeddict-item]
    if "LimitsByRole" in data:
        import aws_sdk_opensearch.types.limits_by_role

        out["limits_by_role"] = (
            aws_sdk_opensearch.types.limits_by_role.deserialize_json(
                data["LimitsByRole"]
            )
        )
    return out
