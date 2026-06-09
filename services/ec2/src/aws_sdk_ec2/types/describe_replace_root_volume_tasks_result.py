"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReplaceRootVolumeTasksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_root_volume_tasks
    import aws_sdk_ec2.types.string


class DescribeReplaceRootVolumeTasksResult(TypedDict):
    replace_root_volume_tasks: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_tasks.ReplaceRootVolumeTasks"
    ]
    """<p>Information about the root volume replacement task.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReplaceRootVolumeTasksResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "replace_root_volume_tasks" in value:
        import aws_sdk_ec2.types.replace_root_volume_tasks

        aws_sdk_ec2.types.replace_root_volume_tasks.serialize_ec2_query(
            value["replace_root_volume_tasks"],
            pairs,
            f"{prefix}.ReplaceRootVolumeTaskSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeReplaceRootVolumeTasksResult:
    out: DescribeReplaceRootVolumeTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("ReplaceRootVolumeTaskSet") is not None:
        import aws_sdk_ec2.types.replace_root_volume_tasks

        out["replace_root_volume_tasks"] = (
            aws_sdk_ec2.types.replace_root_volume_tasks.deserialize_ec2_query(
                el, "ReplaceRootVolumeTaskSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
