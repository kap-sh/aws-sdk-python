"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportImageTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_task_list
    import aws_sdk_ec2.types.string


class DescribeImportImageTasksResult(TypedDict, closed=True):
    import_image_tasks: NotRequired[
        "aws_sdk_ec2.types.import_image_task_list.ImportImageTaskList"
    ]
    """<p>A list of zero or more import image tasks that are currently active or were completed or canceled in the previous 7 days.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImportImageTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "import_image_tasks" in value:
        import aws_sdk_ec2.types.import_image_task_list

        aws_sdk_ec2.types.import_image_task_list.serialize_ec2_query(
            value["import_image_tasks"], pairs, f"{prefix}.ImportImageTaskSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeImportImageTasksResult:
    out: DescribeImportImageTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("ImportImageTaskSet") is not None:
        import aws_sdk_ec2.types.import_image_task_list

        out["import_image_tasks"] = (
            aws_sdk_ec2.types.import_image_task_list.deserialize_ec2_query(
                el, "ImportImageTaskSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
