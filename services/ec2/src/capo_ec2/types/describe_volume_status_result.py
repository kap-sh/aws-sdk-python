"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumeStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.volume_status_list


class DescribeVolumeStatusResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    volume_statuses: NotRequired["capo_ec2.types.volume_status_list.VolumeStatusList"]
    """<p>Information about the status of the volumes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumeStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "volume_statuses" in value:
        import capo_ec2.types.volume_status_list

        capo_ec2.types.volume_status_list.serialize_ec2_query(
            value["volume_statuses"], pairs, f"{key_prefix}VolumeStatusSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVolumeStatusResult:
    out: DescribeVolumeStatusResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("VolumeStatusSet") is not None:
        import capo_ec2.types.volume_status_list

        out["volume_statuses"] = (
            capo_ec2.types.volume_status_list.deserialize_ec2_query(
                el, "VolumeStatusSet"
            )
        )
    return out
