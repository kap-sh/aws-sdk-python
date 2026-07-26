"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceImageMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_image_metadata_list
    import capo_ec2.types.string


class DescribeInstanceImageMetadataResult(TypedDict, closed=True):
    instance_image_metadata: NotRequired[
        "capo_ec2.types.instance_image_metadata_list.InstanceImageMetadataList"
    ]
    """<p>Information about the instance and the AMI used to launch the instance.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceImageMetadataResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_image_metadata" in value:
        import capo_ec2.types.instance_image_metadata_list

        capo_ec2.types.instance_image_metadata_list.serialize_ec2_query(
            value["instance_image_metadata"],
            pairs,
            f"{prefix}.InstanceImageMetadataSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceImageMetadataResult:
    out: DescribeInstanceImageMetadataResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceImageMetadataSet") is not None:
        import capo_ec2.types.instance_image_metadata_list

        out["instance_image_metadata"] = (
            capo_ec2.types.instance_image_metadata_list.deserialize_ec2_query(
                el, "InstanceImageMetadataSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
