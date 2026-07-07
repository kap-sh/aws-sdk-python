"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_list


class DescribeVolumesResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    volumes: NotRequired["aws_sdk_ec2.types.volume_list.VolumeList"]
    """<p>Information about the volumes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "volumes" in value:
        import aws_sdk_ec2.types.volume_list

        aws_sdk_ec2.types.volume_list.serialize_ec2_query(
            value["volumes"], pairs, f"{prefix}.VolumeSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVolumesResult:
    out: DescribeVolumesResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("VolumeSet") is not None:
        import aws_sdk_ec2.types.volume_list

        out["volumes"] = aws_sdk_ec2.types.volume_list.deserialize_ec2_query(
            el, "VolumeSet"
        )
    return out
