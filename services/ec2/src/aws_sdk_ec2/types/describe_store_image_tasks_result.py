"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeStoreImageTasksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.store_image_task_result_set
    import aws_sdk_ec2.types.string


class DescribeStoreImageTasksResult(TypedDict):
    store_image_task_results: NotRequired[
        "aws_sdk_ec2.types.store_image_task_result_set.StoreImageTaskResultSet"
    ]
    """<p>The information about the AMI store tasks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeStoreImageTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "store_image_task_results" in value:
        import aws_sdk_ec2.types.store_image_task_result_set

        aws_sdk_ec2.types.store_image_task_result_set.serialize_ec2_query(
            value["store_image_task_results"],
            pairs,
            f"{prefix}.StoreImageTaskResultSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeStoreImageTasksResult:
    out: DescribeStoreImageTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("StoreImageTaskResultSet") is not None:
        import aws_sdk_ec2.types.store_image_task_result_set

        out["store_image_task_results"] = (
            aws_sdk_ec2.types.store_image_task_result_set.deserialize_ec2_query(
                el, "StoreImageTaskResultSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
