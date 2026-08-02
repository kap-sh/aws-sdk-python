"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesModificationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.volume_modification_list


class DescribeVolumesModificationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    volumes_modifications: NotRequired[
        "capo_ec2.types.volume_modification_list.VolumeModificationList"
    ]
    """<p>Information about the volume modifications.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumesModificationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "volumes_modifications" in value:
        import capo_ec2.types.volume_modification_list

        capo_ec2.types.volume_modification_list.serialize_ec2_query(
            value["volumes_modifications"], pairs, f"{key_prefix}VolumeModificationSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVolumesModificationsResult:
    out: DescribeVolumesModificationsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("VolumeModificationSet") is not None:
        import capo_ec2.types.volume_modification_list

        out["volumes_modifications"] = (
            capo_ec2.types.volume_modification_list.deserialize_ec2_query(
                el, "VolumeModificationSet"
            )
        )
    return out
