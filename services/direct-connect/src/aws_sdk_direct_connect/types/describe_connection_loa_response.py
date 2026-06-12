"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeConnectionLoaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.loa


class DescribeConnectionLoaResponse(TypedDict):
    loa: NotRequired["aws_sdk_direct_connect.types.loa.Loa"]
    """<p>The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionLoaResponse) -> dict:
    out: dict = {}
    if "loa" in value:
        import aws_sdk_direct_connect.types.loa

        out["loa"] = aws_sdk_direct_connect.types.loa.serialize_aws_json_1_1(
            value["loa"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionLoaResponse:
    out: DescribeConnectionLoaResponse = {}  # type: ignore[typeddict-item]
    if "loa" in data:
        import aws_sdk_direct_connect.types.loa

        out["loa"] = aws_sdk_direct_connect.types.loa.deserialize_aws_json_1_1(
            data["loa"]
        )
    return out
