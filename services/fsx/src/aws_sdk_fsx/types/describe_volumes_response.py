"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeVolumesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.next_token
    import aws_sdk_fsx.types.volumes


class DescribeVolumesResponse(TypedDict, closed=True):
    volumes: NotRequired["aws_sdk_fsx.types.volumes.Volumes"]
    """<p>Returned after a successful <code>DescribeVolumes</code> operation, describing each volume.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVolumesResponse) -> dict:
    out: dict = {}
    if "volumes" in value:
        import aws_sdk_fsx.types.volumes

        out["Volumes"] = aws_sdk_fsx.types.volumes.serialize_aws_json_1_1(
            value["volumes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVolumesResponse:
    out: DescribeVolumesResponse = {}  # type: ignore[typeddict-item]
    if "Volumes" in data:
        import aws_sdk_fsx.types.volumes

        out["volumes"] = aws_sdk_fsx.types.volumes.deserialize_aws_json_1_1(
            data["Volumes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
