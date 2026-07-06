"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeBundleTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bundle_task_list


class DescribeBundleTasksResult(TypedDict, closed=True):
    bundle_tasks: NotRequired["aws_sdk_ec2.types.bundle_task_list.BundleTaskList"]
    """<p>Information about the bundle tasks.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeBundleTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "bundle_tasks" in value:
        import aws_sdk_ec2.types.bundle_task_list

        aws_sdk_ec2.types.bundle_task_list.serialize_ec2_query(
            value["bundle_tasks"], pairs, f"{prefix}.BundleInstanceTasksSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeBundleTasksResult:
    out: DescribeBundleTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("BundleInstanceTasksSet") is not None:
        import aws_sdk_ec2.types.bundle_task_list

        out["bundle_tasks"] = aws_sdk_ec2.types.bundle_task_list.deserialize_ec2_query(
            el, "BundleInstanceTasksSet"
        )
    return out
