"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesModificationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_modification_list


class DescribeVolumesModificationsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    volumes_modifications: NotRequired[
        "aws_sdk_ec2.types.volume_modification_list.VolumeModificationList"
    ]
    """<p>Information about the volume modifications.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumesModificationsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "volumes_modifications" in value:
        import aws_sdk_ec2.types.volume_modification_list

        aws_sdk_ec2.types.volume_modification_list.serialize_ec2_query(
            value["volumes_modifications"], pairs, f"{prefix}.VolumeModificationSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVolumesModificationsResult:
    out: DescribeVolumesModificationsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("VolumeModificationSet") is not None:
        import aws_sdk_ec2.types.volume_modification_list

        out["volumes_modifications"] = (
            aws_sdk_ec2.types.volume_modification_list.deserialize_ec2_query(
                el, "VolumeModificationSet"
            )
        )
    return out
